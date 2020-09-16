import pandas as pd
import numpy as np

def k_user_interactions(data, K):
    data.sort_values(by='timestamp', ascending=True, inplace=True)
    data.drop_duplicates(subset=['user', 'item'], keep='last', inplace=True)
    num_users = len(pd.unique(data.user))
    num_items = len(pd.unique(data.item))

    print('initial user, item:', num_users, num_items)

    # filter users
    data, num_items_by_user = filter_user(data, K)

    num_users = len(pd.unique(data.user))
    

    # filter items
    data, num_users_by_item = filter_item(data, 1)

    num_items = len(pd.unique(data.item))
    print('after filter :', num_users, num_items)

    # assign new user id
    user_frame = num_items_by_user
    user_frame.columns = ['item_cnt']
    user_frame['new_id'] = list(range(num_users))

    frame_dict = user_frame.to_dict()
    user_id_dict = frame_dict['new_id']
    user_frame = user_frame.set_index('new_id')
    user_to_num_items = user_frame.to_dict()['item_cnt']

    data.user = [user_id_dict[x] for x in  data.user.tolist()]
    
    # assign new item id
    item_frame = num_users_by_item
    item_frame.columns = ['user_cnt']
    item_frame['new_id'] = range(num_items)

    frame_dict = item_frame.to_dict()
    item_id_dict = frame_dict['new_id']
    item_frame = item_frame.set_index('new_id')
    item_to_num_users = item_frame.to_dict()['user_cnt']

    data.item = [item_id_dict[x] for x in  data.item.tolist()]

    return data

def k_core(data, K):
    data.sort_values(by='timestamp', ascending=True, inplace=True)
    data.drop_duplicates(subset=['user', 'item'], keep='last', inplace=True)
    num_users = len(pd.unique(data.user))
    num_items = len(pd.unique(data.item))

    print('initial user, item:', num_users, num_items)

    user_changed = True
    item_changed = True
    idx = 1
    while (user_changed or item_changed):
        user_changed = False
        item_changed = False

        # filter users
        data, num_items_by_user = filter_user(data, K)
        new_num_users = len(pd.unique(data.user))
        print(f'cycle {idx} U {num_users} -> {new_num_users}')
        if num_users != new_num_users:
            user_changed = True
            num_users = new_num_users
        
        # filter items
        data, num_users_by_item = filter_item(data, K)
        new_num_items = len(pd.unique(data.item))
        print(f'cycle {idx} I {num_items} -> {new_num_items}')
        if num_items != new_num_items:
            item_changed = True
            num_items = new_num_items

        idx += 1

        print(user_changed, item_changed)

    # assign new user id
    user_frame = num_items_by_user
    user_frame.columns = ['item_cnt']
    user_frame['new_id'] = list(range(num_users))

    frame_dict = user_frame.to_dict()
    user_id_dict = frame_dict['new_id']
    user_frame = user_frame.set_index('new_id')
    user_to_num_items = user_frame.to_dict()['item_cnt']

    data.user = [user_id_dict[x] for x in  data.user.tolist()]
    
    # assign new item id
    item_frame = num_users_by_item
    item_frame.columns = ['user_cnt']
    item_frame['new_id'] = range(num_items)

    frame_dict = item_frame.to_dict()
    item_id_dict = frame_dict['new_id']
    item_frame = item_frame.set_index('new_id')
    item_to_num_users = item_frame.to_dict()['user_cnt']

    data.item = [item_id_dict[x] for x in  data.item.tolist()]

    return data

def filter_user(data, min_n):
    num_items_by_user = data.groupby('user', as_index=False).size()
    user_filter_idx = data['user'].isin(num_items_by_user[num_items_by_user['size'] >= min_n]['user'])
    data = data[user_filter_idx]
    num_items_by_user = data.groupby('user', as_index=False).size()
    num_items_by_user = num_items_by_user.set_index('user')

    return data, num_items_by_user

def filter_item(data, min_n):
    num_users_by_item = data.groupby('item', as_index=False).size()
    item_filter_idx = data['item'].isin(num_users_by_item[num_users_by_item['size'] >= min_n]['item'])
    data = data[item_filter_idx]
    num_users_by_item = data.groupby('item', as_index=False).size()
    num_users_by_item = num_users_by_item.set_index('item')

    return data, num_users_by_item