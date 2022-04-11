# Fisher's Iris data set analysis
# Author: Tanja Juric

# First, I wanted to add the column names to the data, found it here:
# URL: https://datascience.stackexchange.com/questions/45314/dataframe-has-no-column-names-how-to-add-a-header
# Used pandas to read csv and assigned the names to the columns
# Took the data set and the description of it from here:
# URL: https://archive.ics.uci.edu/ml/datasets/iris

import pandas as pd

irisData = pd.read_csv('iris.csv', sep =',', names=['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'])
#irisData is actually a data frame

#print(irisData)
#irisData.shape #this tells me how many rows and columns there are

# .head() shows the first five lines to see how will data display; it's a method 
# URL: https://www.w3resource.com/pandas/dataframe/dataframe-head.php
#print(irisData.head(4)) 

# pandas and data frames nicely explained; for now I am trying things from here:
# URL https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/

'''
print(type(irisData)) #says that irisData is a data frame
print(irisData.dtypes) #types od data inside data frame

print(irisData.tail(2)) #shows last two rows
'''

#print(irisData.columns)

print(pd.unique(irisData['species'])) #to see how many unique values in the column species, returns a list

print(irisData['petal_length'].describe())     #to get basic statistics for a column

print("Minimum value of petal length is:", irisData['petal_length'].min(), "cm")

#summarize by variable; .groupby method
groupedSpecies = irisData.groupby('species')
print(groupedSpecies.describe())
print("The means of species are:\n")
print(groupedSpecies.mean())