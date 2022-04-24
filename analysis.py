# Fisher's Iris data set analysis
# Author: Tanja Juric

# First, I wanted to add the column names to the data, found it here:
# URL: https://datascience.stackexchange.com/questions/45314/dataframe-has-no-column-names-how-to-add-a-header
# Used pandas to read csv and assigned the names to the columns
# Took the data set and the description of it from here:
# URL: https://archive.ics.uci.edu/ml/datasets/iris

from os import stat_result
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

irisData = pd.read_csv('iris.csv', sep =',', names=['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'])
#irisData is actually a data frame

print(irisData)
irisData.shape #this tells me how many rows and columns there are

#.head() shows the first five lines to see how will data display; it's a method 
# URL: https://www.w3resource.com/pandas/dataframe/dataframe-head.php
print(irisData.head(4)) 

# pandas and data frames nicely explained; for now I am trying things from here:
# URL https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/


print(type(irisData)) #says that irisData is a data frame
print(irisData.dtypes) #types od data inside data frame

print(irisData.tail(2)) #shows last two rows


print(irisData.columns)


print(pd.unique(irisData['species'])) #to see how many unique values in the column species, returns a list

petal_length_stats = irisData['petal_length'].describe()     #to get basic statistics for a column
print(petal_length_stats)

print("Minimum value of petal length is:", irisData['petal_length'].min(), "cm")


#summarize by variable; .groupby method
groupedSpecies = irisData.groupby('species')
print(groupedSpecies.describe())
print("The means of species are:\n")
mean = groupedSpecies.mean()
print(mean)

groupedSpecies2 = irisData.groupby(['sepal_length', 'species']) #to group by 2 variables
print(groupedSpecies2.mean())

print(irisData['sepal_length'].describe())


# summary counts
# groupby and count() method together
counts = irisData.groupby('species')['species'].count()
#counts = irisData.groupby('sepal_length')['sepal_length'].count()
print(counts)

#counts = irisData.groupby('species')['species'].count()['Iris-setosa']
#print(counts)


stats = groupedSpecies.describe()
print(stats)

# trying to print results into a textfile
filename = 'allstats.txt'
with open(filename, 'w+t') as f:
    f.write(str("Basic statistics for petal length") + "\n" + str(petal_length_stats) + "\n\n" + str(mean) + "\n\n" + str(counts) + "\n\n" + str(stats))
    #f.write(str(counts))

#https://stackoverflow.com/questions/65202315/print-variable-to-txt-file
#https://stackoverflow.com/questions/27324159/how-to-write-a-blank-line-to-a-text-file

