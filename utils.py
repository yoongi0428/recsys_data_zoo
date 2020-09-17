import pandas as pd
import numpy as np
import scipy.integrate as integrate
import scipy.sparse as sparse
from datetime import datetime
import time
import json
from tqdm import tqdm

def load_raw_df(dataset, data_to_file, data_to_sep):
    if dataset in ['amusic', 'acd', 'acna', 'agames']:
        return load_amusic_df(data_to_file[dataset])
    elif dataset == 'gowalla':
        return load_gowalla_df(data_to_file[dataset], data_to_sep[dataset])
    elif dataset == 'citeulike':
        return load_citeulike_df(data_to_file[dataset], data_to_sep[dataset])
    elif dataset in ['epinions', 'pinterest', 'yelp2018']:
        return load_epinions_df(data_to_file[dataset], data_to_sep[dataset])

    skiprows = 1 if dataset in ['ml-20m', 'ml-25m'] else None
    df = pd.read_csv(data_to_file[dataset], sep=data_to_sep[dataset], names=['user', 'item', 'ratings', 'timestamp'], skiprows=skiprows)
    df['ratings'] = np.ones(len(df))
    return df

def load_citeulike_df(filepath, sep):
    with open(filepath, 'rt') as f:
        lines = f.readlines()
    users = []
    items = []
    for u, line in enumerate(lines):
        line = line.strip().split(sep)
        num_cite = int(line[0])
        u_items = line[1:]
        if num_cite == 0:
            continue
        users += [u] * num_cite
        items += u_items
    ratings = [1] * len(users)
    timestamps = [1] * len(users)
    df_dict = {
        'user': users,
        'item': items,
        'ratings': ratings,
        'timestamp': timestamps
    }
    df = pd.DataFrame(df_dict)
    return df

def load_epinions_df(filepath, sep):
    df = pd.read_csv(filepath, sep=sep, names=['user', 'item', 'ratings'], skiprows=1).dropna()
    df['ratings'] = np.ones(len(df))
    df['timestamp'] = np.ones(len(df))
    return df

def load_gowalla_df(filepath, sep):
    df = pd.read_csv(filepath, sep=sep, names=['user', 'timestamp', 'latitude', 'longitude', 'item'])
    df['timestamp'] = df['timestamp'].apply(process_time)
    df['ratings'] = np.ones(len(df))
    df = df.loc[:, ['user', 'item', 'ratings', 'timestamp']]
    return df

def load_yelp_df(filepath):
    with open(filepath, 'rt') as f:
        lines = f.readlines()

    users = []
    items = []
    # ratings = []
    timestamps = []
    for line in tqdm(lines, total=len(lines)):
        d = json.loads(line)
        
        users.append(d['user_id'])
        items.append(d['business_id'])
        # ratings.append(d['stars'])
        t = d['date']
        date_arr = time.strptime(t, "%Y-%m-%d %H:%M:%S")
        timestamps.append(int(time.mktime(date_arr)))
    
    ratings = [1] * len(users)
    df_dict = {
        'user': users,
        'item': items,
        'ratings': ratings,
        'timestamp': timestamps
    }
    df = pd.DataFrame(df_dict)
    return df

def load_amusic_df(filepath):
    with open(filepath, 'rt') as f:
        lines = f.readlines()

    users = []
    items = []
    # ratings = []
    timestamps = []
    for line in tqdm(lines, total=len(lines)):
        d = json.loads(line)
        
        users.append(d['reviewerID'])
        items.append(d['asin'])
        # ratings.append(d['overall'])
        timestamps.append(d['unixReviewTime'])
    
    ratings = [1] * len(users)
    df_dict = {
        'user': users,
        'item': items,
        'ratings': ratings,
        'timestamp': timestamps
    }
    df = pd.DataFrame(df_dict)
    return df

def load_ciao_df(filepath, sep):
    df = pd.read_csv(filepath, sep=sep, names=['user', 'item'], skiprows=1).dropna()
    df['ratings'] = np.ones(len(df))
    df['timestamp'] = np.ones(len(df))
    return df

def process_time(time_str):
    standard_time_list = list(time_str)
    standard_time_list[10] = " "
    standard_time_list.pop()
    standard_time = "".join(standard_time_list)
    date_arr = time.strptime(standard_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(date_arr))
    return timestamp

def df_to_sparse(df, shape):
    rows, cols = df.user, df.item
    values = df.ratings

    sp_data = sparse.csr_matrix((values, (rows, cols)), dtype='float64', shape=shape)

    num_nonzeros = np.diff(sp_data.indptr)
    rows_to_drop = num_nonzeros == 0
    if sum(rows_to_drop) > 0:
        print('%d empty users are dropped from matrix.' % sum(rows_to_drop))
        sp_data = sp_data[num_nonzeros != 0]

    return sp_data

def dist_lorentz(x):
    y = np.array(x)           # y-axis data
    y = np.sort(y, kind='mergesort')

    x = np.repeat(1, len(y))  # x-axis data

    pct_x = x / sum(x)        # x normalized
    pct_x = np.cumsum(pct_x)  # CDF x

    pct_y = y / sum(y)        # y normalized
    pct_y = np.cumsum(pct_y)  # CDF y

    # starts with (0,0)
    pct_y = np.insert(pct_y, 0, 0) 
    pct_x = np.insert(pct_x, 0, 0)

    return pct_x, pct_y

def gini(x):
    x, y = dist_lorentz(x)

    B = integrate.trapz(y, x)   # area under lorentz curve
    AB = 0.5                    # area under bisetrix curve
    A = AB - B                  # area between lorentz and bisetrix
    res = A / AB                # gini index

    return res

def get_stat_dict(rating_matrix):
    NUM_USERS, NUM_ITEMS = rating_matrix.shape
    NUM_RATINGS = rating_matrix.nnz
    NUM_RATINGS_PER_USER = NUM_RATINGS / NUM_USERS

    DENSITY = NUM_RATINGS / (NUM_USERS * NUM_ITEMS)
    SPARSITY = 1 - DENSITY
    SHAPE = NUM_USERS / NUM_ITEMS
    
    user_popularity = rating_matrix.sum(1).A.reshape(-1)
    item_popularity = rating_matrix.sum(0).A.reshape(-1)

    sorted_user_popularity = np.sort(user_popularity)
    sorted_item_popularity = np.sort(item_popularity)

    GINI_USER = gini(sorted_user_popularity)
    GINI_ITEM = gini(sorted_item_popularity)

    CONCENTRATION = sum(sorted_item_popularity[-int(len(item_popularity) * 0.05):]) / NUM_RATINGS

    ret = {
        '# Users': NUM_USERS,
        '# Items': NUM_ITEMS,
        '# Ratings': NUM_RATINGS,
        '# Ratings per user': NUM_RATINGS_PER_USER,
        'Sparsity': SPARSITY,
        'Shape': SHAPE,
        'Gini User': GINI_USER,
        'Gini Item': GINI_ITEM,
        'Concen.': CONCENTRATION
    }
    return ret