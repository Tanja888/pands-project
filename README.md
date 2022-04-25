### pands-project
## Analysis of Fisher's Iris data set using Python 
For the purpose of this project we used the multivariate Iris flower data set commonly used in statistical analysis and machine learning, also described as "Hello World for data science"[¹][1]. These data were collected by botanist E. Anderson and used for linear discriminant analysis of three species of the flower by biologist and statistician R.A. Fisher in 1936.[²][2] The research showed that Iris Setosa is linearly separable from Iris Virginica and Iris Versicolor.[³][3] Data set was taken from UCI Machine Learning Repository.[⁴][4]

## Technologies
Python 3.9.7

## Data 
Iris data set includes three classes: Iris Setosa, Iris Versicolor and Iris Virginica with 4 attributes measured in centimeters: sepal length, sepal width, petal length and petal width. The total number of instances is 150.

## Setup
Three libraries were needed for the analysis:
```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
```

## Sneak peek into data set 
### Data import
First, we had to import the csv file using pandas to get the 'irisData' data frame.
```python
    irisData = pd.read_csv('iris.csv', sep =',', names=['sepal_length' , 'sepal_width' , 
    'petal_length' , 'petal_width' , 'species'])
```
### Describing data
We used methods to: check the shape of the data, get the first few and the last few rows and see the columns: 
```python
    irisData.shape
    irisData.head(4)
    irisData.tail(4)
    irisData.column
```

To show the types of data we are dealing with we used the type class and dtypes method.
```python
    type(irisData)
    irisData.dtypes
```

We also checked for unique values inside the species and if there are any null values in the set
```python
    pd.unique(irisData['species'])
    irisData.isnull()
```

## 2. Statistics and Data Visualization 
By using the groupby and count method, we checked how many of each species there are
```python 
    counts = irisData.groupby('species')['species'].count()
```

Summary statistics for each variable using describe method; 
```python
    sl_stats = irisData['sepal_length'].describe()
```

All of the summary statistics are outputting into .txt file 'allstats.txt'
```python
    filename = 'allstats.txt'
with open(filename, 'w+t') as f:
    f.write(str(counts) + ... + str(pw_stats))
```

## References
[1]: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/        
[2]: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5    
[3]: https://en.wikipedia.org/wiki/Iris_flower_data_set  
[4]: https://archive.ics.uci.edu/ml/datasets/iris    

1:  https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/  
2:  https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  
3:  https://archive.ics.uci.edu/ml/datasets/iris  
4:  https://en.wikipedia.org/wiki/Iris_flower_data_set   
5:  https://datascience.stackexchange.com/questions/45314/dataframe-has-no-column-names-how-to-add-a-header  
6:  https://www.w3resource.com/pandas/dataframe/dataframe-head.php  
7:  https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/  
8:  https://chartio.com/resources/tutorials/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe/  
9:  https://stackoverflow.com/questions/65202315/print-variable-to-txt-file    
10: https://stackoverflow.com/questions/27324159/how-to-write-a-blank-line-to-a-text-file 



## Further reading


## To-do - I divided the project into these tasks:
- [x] about Fisher's Iris data set
- [ ] import data and run some statistics
- [x] export analysis to text file
- [ ] create histograms
- [ ] create scatter plot
- [ ] conclusions 
- [ ] make a nice readme and add references