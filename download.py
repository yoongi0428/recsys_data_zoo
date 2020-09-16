import os
import argparse
import requests

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
    'epinions': 'http://www.trustlet.org/datasets/downloaded_epinions/ratings_data.txt.bz2',
    'gowalla': 'https://snap.stanford.edu/data/loc-gowalla_totalCheckins.txt.gz',
    'citeulike': 'https://raw.githubusercontent.com/js05212/citeulike-a/master/users.dat',
    'pinterest': 'https://github.com/hexiangnan/neural_collaborative_filtering/raw/master/Data/pinterest-20.train.rating',  # NCF
    'yelp': 'https://github.com/xiangwang1223/knowledge_graph_attention_network/raw/master/Data/yelp2018/train.txt'         # yelp-2018
}

def check_availability(dataset):
    if dataset in dataset_to_urls:
        print(f'{dataset} is available. Download it directly.')
    else:
        print(f'Cannot download {dataset} directly. Please download it from web.')
        exit(1)


def download_file(dataset, base_dir):
    check_availability(dataset)

    url = dataset_to_urls[dataset]
    
    data_dir = os.path.join(base_dir, dataset)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    local_filename = os.path.join(data_dir, url.split('/')[-1])

    # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests/16696317#16696317
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename
# "doc.id","title","citeulike.id","raw.title","raw.abstract"
if __name__ == '__main__':
    # Download
    local_filepath = download_file(args.dataset, args.data_dir)
    print(f'[COMPLETE] {args.dataset} is downloaded into {local_filepath}!')