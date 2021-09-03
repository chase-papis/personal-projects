import numpy as np
import pandas as pd

print('imported')


#CREATING, READING, WRITING [KAGGLE]


#data frame is a table - entries which have values ( 'entry':[value(s)]}

pd.DataFrame(
    {'Yes': [50, 21],
     'No': [131, 2]}
)

#result:
# __| yes | no |
# 0 | 50  | 131|
# 1 | 21  | 2  |

#50 = yes[0]
# 2 = no[1]



pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']})


#result:
# __|     bob      |     sue     |
# 0 |  i liked it  | pretty good |
# 1 | it was awful |    bland    |

#these are dataframe objects
#syntax is a dictionary - keys are column names, values are list of entries

#index can be changed:

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.'],
              index=['Product A', 'Product B']})



#index will now be product a/b instead of 0/1


#series is a list (sequence of data values)/single column of a dataframe


pd.Series([1, 2, 3, 4, 5])

#output: 
#0  1
#1  2
#2  3
#3  4
#4  5
#dtype: int64



pd.Series([30, 35, 40],
          index=['2015 Sales',
                 '2016 Sales',
                 '2017 Sales'],
          name='Product A')

#output:
#2015 Sales    30
#2016 Sales    35
#2017 Sales    40
#Name: Product A, dtype: int64


#CSV files example:
#Product A,Product B,Product C,
#30,21,9,
#35,34,1,
#41,11,11

#csv file - table of values separated by commas (comma-separated values)


wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

wine_reviews.shape #how large the dataframe is
#(129971, 14)

#130,000 records split across 14 different columns

wine_reviews.head()
#examines contents but only grabs first 5 rows




























