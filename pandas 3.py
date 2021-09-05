import pandas as pd
import numpy as np

#SUMMARY FUNCTIONS AND MAP


pd.set_option('max_rows', 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv",
                      index_col=0)

reviews

#output: table of wine reviews with an index column starting at 0



#Summary functions

#summary functions restructure data in a useful way

reviews.points.describe()

#output:
#count    129971.000000
#mean         88.447138
#             ...      
#75%          91.000000
#max         100.000000
#Name: points, Length: 8, dtype: float64

#describe() produces a high-level summary of attributes of the given column
#type aware - output changes based on data type


#for string data:

reviews.taster_name.describe()

#output:
#count         103727
#unique            19
#top       Roger Voss
#freq           25514
#Name: taster_name, dtype: object


reviews.points.mean()

#output: 88.447138...


#list of unique values

reviews.taster_name.unique()

#output:
#array(['Kerin O’Keefe', 'Roger Voss', 'Paul Gregutt',
       #'Alexander Peartree', 'Michael Schachner', 'Anna Lee C. Iijima',
       #'Virginie Boone', 'Matt Kettmann', nan, 'Sean P. Sullivan',
       #'Jim Gordon', 'Joe Czerwinski', 'Anne Krebiehl\xa0MW',
       #'Lauren Buzzeo', 'Mike DeSimone', 'Jeff Jenssen',
       #'Susan Kostrzewa', 'Carrie Dykes', 'Fiona Adams',
       #'Christina Pickard'], dtype=object)



#see unique values and number of occurences:

reviews.taster_name.value_count()

#output:
#Roger Voss           25514
#Michael Schachner    15134
#                     ...  
#Fiona Adams             27
#Christina Pickard        6
#Name: taster_name, Length: 19, dtype: int64



#Maps

#maps takes a set of values and "maps" them to another set

review_points_mean = review.points.mean()
review.points.map(lambda p: p - review_points_mean)

#output:
#0        -1.447138
#1        -1.447138
#            ...   
#129969    1.552862
#129970    1.552862
#Name: points, Length: 129971, dtype: float64

#lambda function: takes initial points value and subtracts mean
#map function "maps" the new values to the initial values (points)


def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

#apply() transforms whole datafram by calling a custom function on each row
#output: full table where points are now the difference from the mean

#map() and apply() do not modify the original data, only return new, transformed
#series and dataframes.

#using axis='index' in apply() -> the function would need to tranform each column

reviews.head(1)

#output: first row of original table with original points value


review_points_mean = review.points.mean()
review.points - review_points_mean

#output:
#0        -1.447138
#1        -1.447138
#            ...   
#129969    1.552862
#129970    1.552862
#Name: points, Length: 129971, dtype: float64


#combining country and region

reviews.country = ' - ' + reviews.region_1

#output:
#0            Italy - Etna
#1                     NaN
#               ...       
#129969    France - Alsace
#129970    France - Alsace
#Length: 129971, dtype: object

#these functions are faster than map(0 or apply() because they use speed ups
#built in pandas

#all standard Py operators ( >, <, == etc.) work in the same way

#however, not as flexible - map()/apply() can apply conditional logic
