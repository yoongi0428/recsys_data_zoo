# Recommender System Data Collection

## List of Dataset
|    Dataset   	            |      Domain      	| Feedback 	| Timestamp |                       Auxillary information                      	|             Link 	|
|:------------:	        |:----------------:	|:--------:	|:---------:|:----------------------------------------------------------------:	|------	|
|     ML-1M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-10M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-20M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-25M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
| Amazon Music (5-core) |    E-commerce    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://nijianmo.github.io/amazon/index.html)  |
|   Epinions   	        |    E-commerce    	|  Rating  	|     X     |                                 -                                	| [Download](http://www.trustlet.org/datasets/downloaded_epinions/ratings_data.txt.bz2)  |
|     Yelp     	        |    Restaurant    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://www.yelp.com/dataset)  |
|   citeulike  	        | Citation Network 	|   Click  	|     X     |                           Tags of item                           	| [Page](https://github.com/js05212/citeulike-a)  |
|   Pinterest  	        |  Social Network  	|   Click  	|     X     |                Item metadata (e.g. Item category)                	| [Raw](https://sites.google.com/site/xueatalphabeta/academic-projects), [NCF](https://github.com/hexiangnan/neural_collaborative_filtering)  |
|    Gowalla   	|  Social Network  	|   Click  	|     O     	| Relation between users, item metadata (e.g. longitude, latitude) 	| [Page](https://snap.stanford.edu/data/loc-Gowalla.html)  |

## Preprocess Method
### K-minimum User Interactions
    - Filter out users with less than K interactions
    - Filter out items with no interactions
### K-core Setting
    - Filter out users with less than K interactions
    - Filter out items with less than K interactions
    - Repeat until there is no further change in # users and items

## Statistics
### Definitions
    - User Avg. Ratings: (# Ratings) / (# Users)
    - Sparsity: 1 - {(# Ratings) / (# Users * # Items)}
    - Shape: # Users / # Items
    - Gini User/Item: Gini-index of user/item popularity. Ratings are more inequally distributed as the index is close to 1.
    - Item Concen.: (Item Concentration) Ratio of the ratings that top 5% items hold.

### Raw data (data without preprocessing)

### 10-minimum User Interactions

### 20-minimum User Interactions

### 10-core Settings
