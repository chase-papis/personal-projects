import pandas as pd
import numpy as np

#INDEXING, SELECTING & ASSIGNING

#examples using wine reviews ('reviews')



#Native accessors - access property of object by accessing it as an attribute e.g. book.title, car.model

reviews.country

#output:
#0 Italy
#1 Portugal
#...
#129970 France

reviews['country']

#output:
#0 Italy
#1 Portugal
#...
#129970 France
#Name: country, Length: 129971, dtype: object

#with dict. - access values using indexing operator ([])
#e.g book['title'], car['model']

#^ better as it can handle reserved characters like spaces
#car.registration number (does not work) vs car['registration number']

reviews['country'][0]

#output: 'Italy'

reviews['country'][1]

#output: 'Portugal'



#Indexing

#index based selection - selecting data based on numerical position [iloc]

reviews.iloc[0]

#Output:
#country                                                  #  Italy
#description    Aromas include tropical fruit, broom, brimston...
#...
#variety                                              #White Blend
#winery                                                   #Nicosia
#Name: 0, Length: 13, dtype: object

#loc & iloc - row-first column-second
#easier to retrieve rows
#to get column with iloc:

reviews.iloc[:, 0]

#Output:
#0            Italy
#1         Portugal
#...
#129969      France
#129970      France
#Name: country, Length: 129971, dtype: object

# : operator means everything -> all rows, first column

#to get columns from 1st, 2nd, and 3rd rows:

reviews.iloc[:3, 0]

#Ouput:
#0       Italy
#1    Portugal
#2          US
#Name: country, dtype: object

#up to the third row (index 2), first column (countries)

reviews.iloc[1:3, 0]

#Output:
#1    Portugal
#2          US
#Name: country, dtype: object

#rows 2 and 3 (index 1 and 2), first column (countries)

#can also pass a list:

reviews.iloc[[0, 1, 2], 0]

#Output:
#0       Italy
#1    Portugal
#2          US
#Name: country, dtype: object

#can use negatives to get values from the end of the list

reviews.iloc[-5:]

#Output: table with the last 5 rows and all columns



#Label based selection
#loc operator

reviews.loc[0, 'country']  #gets first entry

#Output:
#'Italy'

#iloc is simpler as it ignores dataset's indices
#loc uses index info to do its work
#loc is usually easier if it has meaningful indices, e.g.:

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

#gets all rows and only the specific named columns
#output: 129971 rows x 3 columns

#choosing between loc/iloc

#iloc uses standard indexing - first digit included, last excluded ([0:10 gets indexes 0 to 9])
#loc includes last digit (0:10 gets indexes 0 to 10)

#can be easier/more convenient to use loc for string-based index values



#manipulating the index

reviews.set_index('title')

#set_index can name/set the index, such as if it's not numerical
#e.g here index might be "review titles", so index is named to "titles"



#conditional selection

reviews.country == 'Italy'

#output: index column and country column with True/False 

reviews.loc[reviews.country == 'Italy']

#output: table with all columns, but only rows where reviews.country == 'Italy' is true

#ampersand (&) to bring two queries together

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

#output: table with all columns, but rows that only satisfy both criteria (italian wines with 90 or more points)

#pip (|) used as "or"

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

#output: table with all columns but rows where the country is either italy, the points are >=90, or both


#isin - select data whose value "is in" a list of values

reviews.loc[reviews.country.isin(['Italy', 'France'])]

#output: table gets all rows where the country is italy or france


#isnull (notnull) - highlight values which are (or are not) empty eg. to filter out wines which do not have a price tag

reviews.loc[reviews.price.notnull()]

#output: table with rows where wine prices are not null



#Assigning Data

reviews['critic'] = 'everyone'
reviews['critic']

#output: assigned constant value to the critic column - all rows affected

reviews['index_backwards'] = range(len(reviews), 0, -1))
reviews['index_backwards']

#output: table where the index is reversed
#range of review length, stop = 0, step = -1 (reverses)


