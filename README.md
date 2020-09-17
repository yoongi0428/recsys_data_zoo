# Recommender System Data Collection

## List of Dataset
--------------------
|    Dataset   	            |      Domain      	| Feedback 	| Timestamp |                       Auxillary information                      	|             Link 	|
|:------------:	        |:----------------:	|:--------:	|:---------:|:----------------------------------------------------------------:	|------	|
|     ML-1M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-10M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-20M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
|    ML-25M    	        |       Movie      	|  Rating  	|     O     |         User, movie metadata (e.g. age, gender, genre, …)        	| [Page](https://grouplens.org/datasets/movielens/)  |
| Amazon Music (5-core) |    E-commerce    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://nijianmo.github.io/amazon/index.html)  |
| Amazon CD (5-core) |    E-commerce    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://nijianmo.github.io/amazon/index.html)  |
| Amazon Games (5-core) |    E-commerce    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://nijianmo.github.io/amazon/index.html)  |
| Amazon C&A (5-core) |    E-commerce    	|  Rating  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://nijianmo.github.io/amazon/index.html)  |
| Ciao (5-core) |    E-commerce    	|  Click  	|     O     |    Review text, user, item metadata (e.g. useful votes, style)   	| [Page](https://github.com/pcy1302/TransCF)  |
|   Epinions   	        |    E-commerce    	|  Rating  	|     X     |                                 -                                	| [Download](http://www.trustlet.org/datasets/downloaded_epinions/ratings_data.txt.bz2)  |
|     Yelp-2015     	        |    Restaurant    	|  Rating  	|     -     |    - (Original page is closed)   	| [Page](https://github.com/hexiangnan/sigir16-eals)  |
|     Yelp-2018     	        |    Restaurant    	|  Rating  	|     -     |    - (Original page is closed)   	| [Page](https://github.com/xiangwang1223/knowledge_graph_attention_network/)  |
|   citeulike  	        | Citation Network 	|   Click  	|     X     |                           Tags of item                           	| [Page](https://github.com/js05212/citeulike-a)  |
|   Pinterest  	        |  Social Network  	|   Click  	|     X     |                Item metadata (e.g. Item category)                	| [Raw](https://sites.google.com/site/xueatalphabeta/academic-projects), [NCF](https://github.com/hexiangnan/neural_collaborative_filtering)  |
|    Gowalla   	|  Social Network  	|   Click  	|     O     	| Relation between users, item metadata (e.g. longitude, latitude) 	| [Page](https://snap.stanford.edu/data/loc-Gowalla.html)  |

## Preprocess Method
--------------------

### *<u>K-minimum User Interactions</u>*
    - Filter out users with less than K interactions
    - Filter out items with no interactions
### *<u>K-core Setting</u>*
    - Filter out users with less than K interactions
    - Filter out items with less than K interactions
    - Repeat until there is no further change in # users and items

## Statistics
--------------------
### *<u>Definitions</u>*
    - User Avg. Ratings: (# Ratings) / (# Users)
    - Sparsity: 1 - {(# Ratings) / (# Users * # Items)}
    - Shape: # Users / # Items
    - Gini User/Item: Gini-index of user/item popularity. Ratings are more inequally distributed as the index is close to 1.
    - Item Concen.: (Item Concentration) Ratio of the ratings that top 5% items hold.

</br>

### *<u>Raw data (data without preprocessing)</u>*

|        Dataset      	|     # Users    	|      # Items     	|      # Ratings    	|     User Avg. Ratings    	|     Sparsity    	|      Shape    	|     Gini User    	|     Gini Item    	|     Item Concen.    	|
|:-------------------:	|:--------------:	|:----------------:	|:-----------------:	|:------------------------:	|:---------------:	|:-------------:	|:----------------:	|:----------------:	|:-------------------:	|
|         ML-1M       	|      6,040     	|       3,706      	|      1,000,209    	|           165.60         	|      0.9553     	|     1.6298    	|       0.5286     	|       0.6336     	|        0.2828       	|
|        ML-10M       	|      69,878    	|       10,677     	|     10,000,054    	|           143.11         	|      0.9866     	|     6.5447    	|       0.5707     	|       0.8052     	|        0.5165       	|
|        ML-20M       	|     138,493    	|       26,744     	|     20,000,263    	|           144.41         	|      0.9946     	|     5.1785    	|       0.5807     	|       0.9029     	|        0.7141       	|
|        ML-25M       	|     162,541    	|       59,047     	|     25,000,095    	|           153.81         	|      0.9974     	|     2.7527    	|       0.5895     	|       0.9419     	|        0.8445       	|
|     Amazon Music    	|      16,566    	|       11,797     	|       145,292     	|            8.77          	|      0.9993     	|     1.4043    	|       0.3756     	|       0.4315     	|        0.2476       	|
|       Amazon CD     	|     112,395    	|       73,713     	|      1,402,148    	|           12.48          	|      0.9998     	|     1.5248    	|       0.4656     	|       0.5432     	|        0.3353       	|
|      Amazon C&A     	|     157,212    	|       48,186     	|      1,120,771    	|            7.13          	|      0.9999     	|     3.2626    	|       0.2091     	|       0.5875     	|        0.3787       	|
|     Amazon Games    	|      55,223    	|       17,408     	|       473,427     	|            8.57          	|      0.9995     	|     3.1723    	|       0.3230     	|       0.5849     	|        0.3484       	|
|       Epinions      	|      40,163    	|      139,738     	|       664,823     	|           16.55          	|      0.9999     	|     0.2874    	|       0.6763     	|       0.6936     	|        0.5339       	|
|         Ciao        	|      6,762     	|       16,610     	|       146,997     	|           21.74          	|      0.9987     	|     0.4071    	|       0.5518     	|       0.5309     	|        0.3128       	|
|       Yelp 2015     	|      25,677    	|       25,815     	|       696,865     	|           27.14          	|      0.9989     	|     0.9947    	|       0.4509     	|       0.6037     	|        0.3512       	|
|      Yelp   2018    	|      45,919    	|       45,538     	|      1,183,609    	|           25.78          	|      0.9994     	|     1.0084    	|       0.4268     	|       0.5810     	|        0.3458       	|
|        Gowalla      	|     107,092    	|     1,280,969    	|      3,981,334    	|           37.18          	|      0.9999     	|     0.0836    	|       0.6627     	|       0.5390     	|        0.3628       	|
|       CiteULike     	|      5,551     	|       16,980     	|       204,986     	|           36.93          	|      0.9978     	|     0.3269    	|       0.4706     	|       0.3696     	|        0.2098       	|
|       Pinterest     	|      55,187    	|       9,916      	|      1,463,580    	|           26.52          	|      0.9973     	|     5.5655    	|       0.1401     	|       0.4511     	|        0.1899       	|

</br>

### *<u>10-minimum User Interactions</u>*

|        Dataset      	|     # Users    	|      # Items     	|      # Ratings    	|     User Avg. Ratings    	|     Sparsity    	|      Shape    	|     Gini User    	|     Gini Item    	|     Item Concen.    	|
|:-------------------:	|:--------------:	|:----------------:	|:-----------------:	|:------------------------:	|:---------------:	|:-------------:	|:----------------:	|:----------------:	|:-------------------:	|
|         ML-1M       	|      6,040     	|       3,706      	|      1,000,209    	|           165.60         	|      0.9553     	|     1.6298    	|       0.5286     	|       0.6336     	|        0.2828       	|
|        ML-10M       	|      69,878    	|       10,677     	|     10,000,054    	|           143.11         	|      0.9866     	|     6.5447    	|       0.5707     	|       0.8052     	|        0.5165       	|
|        ML-20M       	|     138,493    	|       26,744     	|     20,000,263    	|           144.41         	|      0.9946     	|     5.1785    	|       0.5807     	|       0.9029     	|        0.7141       	|
|        ML-25M       	|     162,541    	|       59,047     	|     25,000,095    	|           153.81         	|      0.9974     	|     2.7527    	|       0.5895     	|       0.9419     	|        0.8445       	|
|     Amazon Music    	|      3,951     	|       11,483     	|       75,044      	|           18.99          	|      0.9983     	|     0.3441    	|       0.3067     	|       0.4505     	|        0.2405       	|
|       Amazon CD     	|      36,487    	|       73,493     	|       933,651     	|           25.59          	|      0.9997     	|     0.4965    	|       0.4448     	|       0.5455     	|        0.3296       	|
|      Amazon C&A     	|      21,361    	|       44,416     	|       301,976     	|           14.14          	|      0.9997     	|     0.4809    	|       0.1915     	|       0.5807     	|        0.3479       	|
|     Amazon Games    	|      11,986    	|       17,100     	|       215,645     	|           17.99          	|      0.9989     	|     0.7009    	|       0.2994     	|       0.5833     	|        0.3319       	|
|       Epinions      	|      15,786    	|      132,964     	|       580,752     	|           36.79          	|      0.9997     	|     0.1187    	|       0.4816     	|       0.6768     	|        0.5197       	|
|         Ciao        	|      3,829     	|       15,768     	|       129,798     	|           33.90          	|      0.9979     	|     0.2428    	|       0.4516     	|       0.5267     	|        0.3119       	|
|       Yelp 2015     	|      24,930    	|       25,799     	|       690,381     	|           27.69          	|      0.9989     	|     0.9663    	|       0.4482     	|       0.6038     	|        0.3510       	|
|      Yelp   2018    	|      45,842    	|       45,538     	|      1,182,917    	|           25.80          	|      0.9994     	|     1.0067    	|       0.4267     	|       0.5811     	|        0.3458       	|
|        Gowalla      	|      68,709    	|     1,247,158    	|      3,831,386    	|           55.76          	|      0.9999     	|     0.0551    	|       0.5458     	|       0.5365     	|        0.3612       	|
|       CiteULike     	|      5,551     	|       16,980     	|       204,986     	|           36.93          	|      0.9978     	|     0.3269    	|       0.4706     	|       0.3696     	|        0.2098       	|
|       Pinterest     	|      55,187    	|       9,916      	|      1,463,580    	|           26.52          	|      0.9973     	|     5.5655    	|       0.1401     	|       0.4511     	|        0.1899       	|

</br>

### *<u>20-minimum User Interactions</u>*
|        Dataset      	|     # Users    	|      # Items     	|      # Ratings    	|     User Avg. Ratings    	|     Sparsity    	|      Shape    	|     Gini User    	|     Gini Item    	|     Item Concen.    	|
|:-------------------:	|:--------------:	|:----------------:	|:-----------------:	|:------------------------:	|:---------------:	|:-------------:	|:----------------:	|:----------------:	|:-------------------:	|
|         ML-1M       	|      6,040     	|       3,706      	|      1,000,209    	|           165.60         	|      0.9553     	|     1.6298    	|       0.5286     	|       0.6336     	|        0.2828       	|
|        ML-10M       	|      69,878    	|       10,677     	|     10,000,054    	|           143.11         	|      0.9866     	|     6.5447    	|       0.5707     	|       0.8052     	|        0.5165       	|
|        ML-20M       	|     138,493    	|       26,744     	|     20,000,263    	|           144.41         	|      0.9946     	|     5.1785    	|       0.5807     	|       0.9029     	|        0.7141       	|
|        ML-25M       	|     162,541    	|       59,047     	|     25,000,095    	|           153.81         	|      0.9974     	|     2.7527    	|       0.5895     	|       0.9419     	|        0.8445       	|
|     Amazon Music    	|      1,074     	|       10,116     	|       37,526      	|           34.94          	|      0.9965     	|     0.1062    	|       0.2673     	|       0.4466     	|        0.2298       	|
|       Amazon CD     	|      12,284    	|       71,838     	|       616,845     	|           50.22          	|      0.9993     	|     0.1710    	|       0.4262     	|       0.5472     	|        0.3234       	|
|      Amazon C&A     	|      2,302     	|       25,285     	|       66,772      	|           29.01          	|      0.9989     	|     0.0910    	|       0.1976     	|       0.4593     	|        0.2585       	|
|     Amazon Games    	|      2,734     	|       15,189     	|       97,227      	|           35.56          	|      0.9977     	|     0.1800    	|       0.2826     	|       0.5611     	|        0.3069       	|
|       Epinions      	|      8,693     	|      123,330     	|       482,849     	|           55.54          	|      0.9996     	|     0.0705    	|       0.4192     	|       0.6525     	|        0.4983       	|
|         Ciao        	|      2,075     	|       14,887     	|       105,827     	|           51.00          	|      0.9966     	|     0.1394    	|       0.3814     	|       0.5224     	|        0.3083       	|
|       Yelp 2015     	|      9,788     	|       25,373     	|       489,820     	|           50.04          	|      0.9980     	|     0.3858    	|       0.3972     	|       0.5959     	|        0.3346       	|
|      Yelp   2018    	|      17,137    	|       45,447     	|       806,078     	|           47.04          	|      0.9990     	|     0.3771    	|       0.3768     	|       0.5853     	|        0.3381       	|
|        Gowalla      	|      47,752    	|     1,183,848    	|      3,530,010    	|           73.92          	|      0.9999     	|     0.0403    	|       0.4946     	|       0.5289     	|        0.3558       	|
|       CiteULike     	|      3,097     	|       16,792     	|       171,391     	|           55.34          	|      0.9967     	|     0.1844    	|       0.3939     	|       0.3873     	|        0.2139       	|
|       Pinterest     	|      52,190    	|       9,909      	|      1,408,089    	|           26.98          	|      0.9973     	|     5.2669    	|       0.1359     	|       0.4578     	|        0.1923       	|

</br>

### *<u>10-core Settings</u>*

|        Dataset      	|     # Users    	|     # Items    	|      # Ratings    	|     User Avg. Ratings    	|     Sparsity    	|      Shape    	|     Gini User    	|     Gini Item    	|     Item Concen.    	|
|:-------------------:	|:--------------:	|:--------------:	|:-----------------:	|:------------------------:	|:---------------:	|:-------------:	|:----------------:	|:----------------:	|:-------------------:	|
|         ML-1M       	|      6,040     	|      3,260     	|       998,539     	|           165.32         	|      0.9493     	|     1.8528    	|       0.5285     	|       0.5862     	|        0.2594       	|
|        ML-10M       	|      69,878    	|      9,708     	|      9,995,471    	|           143.04         	|      0.9853     	|     7.1980    	|       0.5706     	|       0.7867     	|        0.4945       	|
|        ML-20M       	|     138,493    	|      15,451    	|     19,964,833    	|           144.16         	|      0.9907     	|     8.9634    	|       0.5802     	|       0.8360     	|        0.5784       	|
|        ML-25M       	|     162,539    	|      24,330    	|     24,890,566    	|           153.14         	|      0.9937     	|     6.6806    	|       0.5881     	|       0.8711     	|        0.6558       	|
|       Amazon CD     	|      21,450    	|      18,398    	|       527,503     	|           24.59          	|      0.9987     	|     1.1659    	|       0.4286     	|       0.4274     	|        0.2351       	|
|     Amazon Games    	|      5,942     	|      3,793     	|       103,778     	|           17.47          	|      0.9954     	|     1.5666    	|       0.2857     	|       0.4028     	|        0.2158       	|
|       Epinions      	|      10,706    	|      8,945     	|       300,303     	|           28.05          	|      0.9969     	|     1.1969    	|       0.4037     	|       0.4950     	|        0.3055       	|
|         Ciao        	|      2,136     	|      2,597     	|       59,884      	|           28.04          	|      0.9892     	|     0.8225    	|       0.3982     	|       0.4063     	|        0.2855       	|
|       Yelp 2015     	|      22,087    	|      14,873    	|       602,517     	|           27.28          	|      0.9982     	|     1.4850    	|       0.4413     	|       0.5121     	|        0.2935       	|
|      Yelp   2018    	|      39,055    	|      25,033    	|       988,768     	|           25.32          	|      0.9990     	|     1.5601    	|       0.4168     	|       0.5065     	|        0.2888       	|
|        Gowalla      	|      29,858    	|      40,988    	|      1,027,464    	|           34.41          	|      0.9992     	|     0.7285    	|       0.4666     	|       0.4346     	|        0.2915       	|
|       CiteULike     	|      3,710     	|      6,468     	|       120,324     	|           32.43          	|      0.9950     	|     0.5736    	|       0.4388     	|       0.3052     	|        0.1818       	|
|       Pinterest     	|      55,164    	|      9,316     	|      1,460,487    	|           26.48          	|      0.9972     	|     5.9214    	|       0.1411     	|       0.4188     	|        0.1819       	|

* All users and items are deleted in Amazon-{music, C&A}