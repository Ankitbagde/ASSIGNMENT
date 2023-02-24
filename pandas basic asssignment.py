#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.


# In[1]:


import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)

print(series)


# In[ ]:


Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it.


# In[2]:


import pandas as pd

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(my_list)

print(series)


# In[ ]:


Q3. Create a Pandas DataFrame that contains the following data:

Then, print the DataFrame.
Name -  Alice Bob Claire
Age   -  25    30    27
Gender- Female Male Female


# In[3]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'female']
}

df = pd.DataFrame(data)

print(df)


# In[ ]:


Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.


# In[ ]:


DataFrame in pandas is a two-dimensional table of data,
where each column can have a different data type (e.g., integer, float, string), 
and each row represents a different observation or record. 
In contrast, a Series is a one-dimensional labeled array that can hold any data type (e.g., integer, float, string, Python objects)


# In[4]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)

print(df)


# In[ ]:


Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
get_ipython().set_next_input('you give an example of when you might use one of these functions');get_ipython().run_line_magic('pinfo', 'functions')


# In[ ]:


Some common functions to manipulate data in a DataFrame include:

head() and tail(): to display the first or last few rows of the DataFrame, respectively
describe(): to generate summary statistics of the DataFrame
sort_values(): to sort the rows of the DataFrame based on one or more columns
groupby(): to group the rows of the DataFrame based on one or more columns and perform aggregate functions (e.g., sum, mean, count) on each group
drop(): to remove rows or columns from the DataFrame
merge(): to combine two or more DataFrames based on a common column


# In[ ]:


get_ipython().set_next_input('Q6. Which of the following is mutable in nature Series, DataFrame, Panel');get_ipython().run_line_magic('pinfo', 'Panel')


# In[ ]:


Series and DataFrame are mutable in nature, whereas Panel is not mutable. 
That means you can change the values in a Series or DataFrame after it has been created, 
but you cannot change the values in a Panel after it has been created.


# In[ ]:


Q7. Create a DataFrame using multiple Series. Explain with an example.


# In[5]:


import pandas as pd

names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages = pd.Series([25, 30, 35, 40])
cities = pd.Series(['New York', 'Paris', 'London', 'Tokyo'])

df = pd.DataFrame({'Name': names, 'Age': ages, 'City': cities})

print(df)


# In[ ]:




