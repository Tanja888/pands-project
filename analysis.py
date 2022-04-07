# Fisher's Iris data set analysis
# Author: Tanja Juric

# First, I wanted to add the column names to the data, found it here:
# URL: https://datascience.stackexchange.com/questions/45314/dataframe-has-no-column-names-how-to-add-a-header
# Used pandas to read csv and assigned the names to the columns
# Took the data set and the description of it from here:
# URL: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd

irisData = pd.read_csv('iris.csv', sep =',', names=['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'])
#print(irisData)
#irisData.shape #this tells me how many rows and columns there are

# .head() shows the first five lines to see how will data display
# URL: https://www.w3resource.com/pandas/dataframe/dataframe-head.php
#irisData.head() 

print(irisData.head(3))
