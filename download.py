import os
import argparse
import requests
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument('--data_dir', type=str, default='data')
args = parser.parse_args()

dataset_to_urls = {
    'ml-1m': 'http://files.grouplens.org/datasets/movielens/ml-1m.zip',
    'ml-10m': 'http://files.grouplens.org/datasets/movielens/ml-10m.zip',
    'ml-20m': 'http://files.grouplens.org/datasets/movielens/ml-20m.zip',
    'ml-25m': 'http://files.grouplens.org/datasets/movielens/ml-25m.zip',
    'amusic': 'http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Digital_Music_5.json.gz',  # 5-core
    'acd': 'http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/CDs_and_Vinyl_5.json.gz',  # 5-core, Hierarchical Gating Networks for Sequential Recommendation
    'acna': 'http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Cell_Phones_and_Accessories_5.json.gz',  # 5-core, Collaborative Translational Metric Learning
    'agames': 'http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Video_Games_5.json.gz',
    'ciao': 'https://github.com/pcy1302/TransCF/raw/master/data/ciao/ratings.dat',
    'epinions': 'http://www.trustlet.org/datasets/downloaded_epinions/ratings_data.txt.bz2',
    'gowalla': 'https://snap.stanford.edu/data/loc-gowalla_totalCheckins.txt.gz',
    'citeulike': 'https://raw.githubusercontent.com/js05212/citeulike-a/master/users.dat',
    'pinterest': ['https://github.com/hexiangnan/neural_collaborative_filtering/raw/master/Data/pinterest-20.train.rating',     # NCF
                'https://github.com/hexiangnan/neural_collaborative_filtering/raw/master/Data/pinterest-20.test.rating'],  
    'yelp2015': 'https://github.com/hexiangnan/sigir16-eals/raw/master/data/yelp.rating',  # NCF
    'yelp2018': ['https://github.com/xiangwang1223/knowledge_graph_attention_network/raw/master/Data/yelp2018/train.txt',
                'https://github.com/xiangwang1223/knowledge_graph_attention_network/raw/master/Data/yelp2018/test.txt']        # yelp-2018
}

def check_availability(dataset):
    if dataset in dataset_to_urls:
        print(f'{dataset} is available. Download it directly.')
    else:
        print(f'Cannot download {dataset} directly. Please download it from web.')
        exit(1)

def download_from_url(target_dir, url):
    # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests/16696317#16696317
    local_filename = os.path.join(target_dir, url.split('/')[-1])
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def download_datasets(dataset, base_dir):
    check_availability(dataset)

    url = dataset_to_urls[dataset]
    
    data_dir = os.path.join(base_dir, dataset)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if isinstance(url, list):
        for _urll in url:
            local_filename = download_from_url(data_dir, _urll)
    else:
        local_filename = download_from_url(data_dir, url)
    return local_filename

if __name__ == '__main__':
    # Download
    local_filepath = download_datasets(args.dataset, args.data_dir)
    print(f'[COMPLETE] {args.dataset} is downloaded into {local_filepath}!')

    users = []
    items = []
    ratings = []
    parent_dir = '/'.join(local_filepath.split('/')[:-1])
    if args.dataset == 'pinterest':
        print('Merge pinterest train/test.')
        with open(os.path.join(parent_dir, 'pinterest-20.train.rating'), 'rt') as f:
            lines = f.readlines()

        for line in lines:
            u, i, r, _ = line.strip().split('\t')
            users.append(u)
            items.append(i)
            ratings.append(r)

        with open(os.path.join(parent_dir, 'pinterest-20.test.rating'), 'rt') as f:
            lines = f.readlines()

        for line in lines:
            u, i, r, _ = line.strip().split('\t')
            users.append(u)
            items.append(i)
            ratings.append(r)

        df = pd.DataFrame({'users': users, 'items': items, 'ratings': ratings})
        df.to_csv(os.path.join(parent_dir, 'pinterest.csv'), index=False, header=False)
    elif args.dataset == 'yelp2018':
        print('Merge yelp2018 train/test.')
        with open(os.path.join(parent_dir, 'train.txt'), 'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip().split(' ')
            u = int(line[0])
            u_items = line[1:]
            
            users += [u] * len(u_items)
            items += u_items

        with open(os.path.join(parent_dir, 'test.txt'), 'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip().split()
            u = int(line[0])
            u_items = line[1:]
            
            users += [u] * len(u_items)
            items += u_items

        ratings = [1] * len(users)

        df = pd.DataFrame({'users': users, 'items': items, 'ratings': ratings})
        df.to_csv(os.path.join(parent_dir, 'yelp.csv'), index=False, header=False)