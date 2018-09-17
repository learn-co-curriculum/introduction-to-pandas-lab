
 # Reading Data with Pandas

## Introduction

In this lab, we will be practicing using pandas to create a dataframe object from data we have in a csv file on *wine*! This will not only be a good opportunity for us to scout out a new bottle to try or to give as our next housewarming present, but it will also help us master dataframes and pandas! 

## Objectives
* Importing Pandas
* Creating a DataFrame
* Reading a CSV

## Instructions
In this lab, we are going to work with a dataset on wines. It contains information on the name, type of grape, average rating, region the grapes are from, etc. Below, follow the instructions below to get the tests in `pytests/test_index` to pass. 

Below, import `pandas` and use it to read the csv file, `majestic_wine_data.csv`. Assign the variable `wine_data_from_csv` to the pandas dataframe object. 
> **Note:** While we can import pandas in different ways, in this lab we want to practice following the convention amongst data scientists. 


```python
# import pandas library here

# assign pandas dataframe to wine_data_from_csv
wine_data_from_csv = None

print(wine_data_from_csv)
```

Now, we might notice that the data has some information missing. This will happen sometimes with our datasets. So, to combat this problem, there is a method we can implement on our dataframe object called `fillna()`. It takes an argument, which is the value we would like to insert anywhere there is information missing from our dataframe. Use this method to fill any places in our dataframe that are missing values (i.e. `False` or `0`). This ensure that if we are attempting to operate on this data, we are always able to keep our data consistent and be sure the datatype we are operating on.


```python
# replace any empty spots with the value zero (0)
# assign the updated dataframe to wine_data_without_na

wine_data_without_na = None

print(wine_data_without_na)
```

Next, let's look at our data and see if it's in a state we can really use it. From what we can see above, it doesn't seem like it makes a lot of sense. Our wine data seems to be a bit fractured and all over the place. We want to have a list of dictionaries, where each dictionary has the same keys and points to each datapoint for its respective bottle of wine. This way, we can start to really look at our information and get it into a format where we can start to more effectively opperate on it (and find the best bottle of wine!).


```python
# use the wine_data_without_na to create a list of dictionaries
# where each dictionary contains all attributes and information for the respective bottle of wine
# (i.e. [{bottle1}, {bottle2}, {bottle3}])

list_of_wine_dicts = None

print(list_of_wine_dicts)
```

Now that we have our wine data in a format that is a bit easier for us to work with, let's start to operate on it. Add code to the following fuction definitions to get the return value indicated in the comments below. 

> **Hint:** The below methods are asking for a list of 5 wines based on rating or number of ratings... To **sort** the list of wines, try to make use of lambda functions and Python's **sorted()** function.


```python
# find_top_5_rated should return a list of the 5 highest rated wines
def find_top_5_rated(list_of_wines):
    # add code here
    pass
```


```python
# find_5_most_rated should return a list of the 5 wines with the highest number of ratings
def find_5_most_rated(list_of_wines):
    # add code here
    pass
```

## Summary

Great work! In this lab, we practiced reading data from a csv file using the Pandas library. Remember to adhere to convention where it makes sense, like using a library or working on a codebase with other programmers. We also looked at using Pandas to fill in any blank values (`NaN`) in our data to make sure we would have consistent and easier data to work with, as well as guard against any bugs in our code. We then used pandas to format our data into a list of dictionaries so that we could more easily operate on it.
