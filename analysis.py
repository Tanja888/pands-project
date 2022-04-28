# Fisher's Iris data set analysis
# Author: Tanja Juric

# Imported three libraries needed for the analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Data
# Data set is in the csv format, having the values separated by commas
# To be able to work with data I used pandas to read the csv file and created the irisData data frame 
# Then, I assigned the names to the variables
# Four of them are numeric describing petals and sepals and one is categorical for the species of the flower

irisData = pd.read_csv('iris.csv', sep =',', names=['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'])
#names=['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'] 

# By printing the new variable irisData we can see that the indexes were assigned to the rows and the names to the columns
print(irisData)

# To see the dimensionality of data frame we can use the shape method; it shows the number of rows and columns
print(irisData.shape)

# To see how data will be displayed, especially with the big amount of data we can use head() method to see the first few rows
print(irisData.head(4))

# Or the tail() for the last few rows
print(irisData.tail(4))

# To see what type of data structure are we dealing with we can use the type class
print(type(irisData)) #says that irisData is a data frame

# To see data types inside the data frame we can use dtypes
# it shows that all variables are float64 except the species
print(irisData.dtypes) 

# We can also check what columns we have
print(irisData.columns)

# To get the unique values inside the species unique() method was used; it returns a list
print(pd.unique(irisData['species']))

# This is from Chartio website, I put the reference in Readme
# Even if we know that there are no missing values, for the sake of practice we can use .isnull() method to check it
# It will show all the rows
print(irisData.isnull()) 
# Also, we can check if there are any missing values
# The result returns in boolean form, True or False
print(irisData.isnull().values.any())
# We can do the sum of missing values and show it for each variable
print(irisData.isnull().sum())
# Or, we can check the sum of all missing values for all the variables
print(irisData.isnull().sum().sum())


# 2. Statistics
# In this part I did some basic statistics and summaries
# First to see how are data distributed based on the species
# I used groupby() and count() methods together

counts = irisData.groupby('species')['species'].count()
# we can get the same with value_counts()
#counts = irisData['species'].value_counts()
print(counts)

# Histogram of distribution of species showed in .png file
plt.hist(irisData['species'], color='#9900ff')
plt.title(label='Distribution of species', color='#b84dff')
plt.savefig("species_count.png")
plt.show()


# Summary statistics for each variable
sl_stats = irisData['sepal_length'].describe()
print(sl_stats)

sw_stats = irisData['sepal_width'].describe()
print(sw_stats)

pl_stats = irisData['petal_length'].describe() 
print(pl_stats)

pw_stats = irisData['petal_width'].describe()
print(pw_stats)

# To output the results into the text file, I created a new file 'allstats.txt'
filename = 'allstats.txt'
with open(filename, 'w+t') as f:
    f.write(str(counts) + "\n\n" + str(sl_stats) + "\n\n" + str(sw_stats) + "\n\n" + str(pl_stats) + "\n\n" + str(pw_stats))


# histograms for each variable separately
# need to add labels and change the colour
plt.hist(irisData['sepal_length'], color='#9900ff')
plt.title(label='Sepal length', color='#b84dff')
plt.savefig("sepal_length.png")
plt.show()

plt.hist(irisData['sepal_width'], color ='#5c0099')
plt.title(label='Sepal width', color='#b84dff')
plt.savefig("sepal_width.png")
plt.show()

plt.hist(irisData['petal_length'], color='#cc80ff')
plt.title(label='Petal length', color='#b84dff')
plt.savefig("petal_length.png")
plt.show()

plt.hist(irisData['petal_width'], color='#ebccff')
plt.title(label='Petal width', color='#b84dff')
plt.savefig("petal_width.png")
plt.show()

# histogram of four variables together
# when we call histograms separately they overlap which is handy for comparison 
plt.hist(irisData['sepal_length'], label='sepal_length', color='#9900ff')
plt.hist(irisData['sepal_width'], label='sepal_width', color='#5c0099')
plt.hist(irisData['petal_length'], label='petal_length', color='#cc80ff')
plt.hist(irisData['petal_width'], label='petal_width', color='#ebccff')
plt.legend()
plt.savefig("all_variables.png")
plt.show()



'''
#print(irisData.describe())

groupedSpecies = irisData.groupby('species')
print(groupedSpecies.describe())

#summarize by variable; .groupby method
groupedSpecies = irisData.groupby('species')
print(groupedSpecies.describe())
print("The means of species are:\n")
mean = groupedSpecies.mean()
print(mean)

#groupedSpecies2 = irisData.groupby(['sepal_length', 'species']) #to group by 2 variables
#print(groupedSpecies2.mean())

#stats = groupedSpecies.describe()
#print(stats)
'''


