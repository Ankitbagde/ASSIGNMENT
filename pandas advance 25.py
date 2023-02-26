#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})


# In[2]:


df


# In[ ]:


Q1.Write a code to print the data present in the second row of the dataframe, df.


# In[3]:


import pandas as pd 

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# Select the second row using .iloc and print it
print(df.iloc[1])


# In[ ]:


get_ipython().set_next_input('Q2.Q2. What is the difference between the functions loc and iloc in pandas.DataFrame');get_ipython().run_line_magic('pinfo', 'pandas.DataFrame')


# In[ ]:


--loc and iloc are both methods in Pandas DataFrame used for selecting subsets of data, 
but they differ in how they interpret the indices used for selection.

--loc is primarily label-based, which means that it uses row and column labels to select data. 
It allows selection of rows or columns using their label names (either a single label or a list of labels). The syntax for loc is:


df.loc[row_label, col_label]
For example, to select the first row and the duration column of a DataFrame df, we can use the following code:

df.loc[0, 'duration']
iloc, on the other hand, is primarily integer position-based, which means that it uses row and column indices to select data. 
It allows selection of rows or columns using their integer positions (either a single integer or a slice of integers). The syntax for iloc is:
    
df.iloc[row_pos, col_pos]
For example, to select the first row and the duration column of a DataFrame df, we can use the following code:

df.iloc[0, 1]
In summary, the key difference between loc and iloc is that loc uses label-based indexing,
while iloc uses integer position-based indexing. 
It's important to use the appropriate method depending on the nature of the data and the type of index being used in the DataFrame.


# In[ ]:


Q.3 Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
then find the output for both new_df.loc[2] and new_df.iloc[2].


# In[ ]:


ANS-To reindex a Pandas DataFrame using the reindex method, you can pass a list of indices to the method. 
Here's how you can do it:

import pandas as pd 

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

reindex = [3, 0, 1, 2]
new_df = df.reindex(reindex)
This code will create a new DataFrame new_df that has the same data as df, 
but with rows in the order specified by the reindex list.

To find the output for new_df.loc[2] and new_df.iloc[2], you can run the following code:


print(new_df.loc[2])
print(new_df.iloc[2])
This will output:


course_name    Big Data
duration              6
Name: 1, dtype: object
course_name    Machine Learning
duration                      3
Name: 0, dtype: object
Note that the output for new_df.loc[2] is the third row of the DataFrame,
since we are using label-based indexing and 2 is the label of the third row. 
The output for new_df.iloc[2] is the second row of the DataFrame, 
since we are using integer position-based indexing and 2 is the index of the third row (counting from 0).


# In[4]:


#DATA FOR FURTHER QUESTIONS:-
import pandas as pd
import numpy as np

# Define the column labels and row labels
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]

# Create a DataFrame with random data and the given column and row labels
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


# In[5]:


df1


# In[ ]:


Q4. Write a code to find the following statistical measurements for the above dataframe df1:
(i) mean of each and every column present in the dataframe.
(ii) standard deviation of column, ‘column_2’


# In[6]:


column_means = df1.mean()
print(column_means)


# In[7]:


column_2_std = df1['column_2'].std()
print(column_2_std)


# In[ ]:


Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
mean of column, column_2.
If you are getting errors in executing it then explain why.
[Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]


# In[8]:


df1.loc[2, 'column_2'] = 'some string'


# In[10]:


df1['column_2'] = pd.to_numeric(df1['column_2'], errors='coerce')
column_2_mean = df1['column_2'].mean()
print(column_2_mean)


# In[ ]:


Q6. What do you understand about the windows function in pandas and list the types of windows
get_ipython().run_line_magic('pinfo', 'functions')


# In[ ]:


In pandas, a window function is a way of applying a function to a rolling window of data in a DataFrame or Series.
A window function allows you to compute a summary statistic over a sliding window of consecutive data points, 
where the size and position of the window can be customized.

The basic syntax for using a window function in pandas is as follows:

df['window_function'] = df['column'].rolling(window=window_size).function_name()
Here, window_size is the size of the rolling window, 
and function_name is the name of the summary statistic you want to compute, such as mean, sum, min, max, or std.

There are several types of window functions in pandas, including:

Rolling window functions: These functions compute a summary statistic over a rolling window of a fixed size. 
    Examples include rolling.mean(), rolling.sum(), rolling.min(), rolling.max(), and rolling.std().

Expanding window functions: These functions compute a summary statistic over all the data up to the current point. 
    Examples include expanding.mean(), expanding.sum(), expanding.min(), expanding.max(), and expanding.std().

Exponentially-weighted window functions: These functions compute a summary statistic over a rolling window, 
    where more recent data points are weighted more heavily than older data points. Examples include ewm.mean(), ewm.min(), ewm.max(), and ewm.std().

Rolling apply functions: These functions allow you to apply a custom function to a rolling window of data.
    Examples include rolling.apply() and rolling.agg().

Window functions are useful for analyzing time series and other sequential data, where the values of one data point depend on the values of nearby data points. By using window functions, you can compute summary statistics that capture trends and patterns in the data, which can help you make better predictions and decisions.


# In[ ]:


Q7. Write a code to print only the current month and year at the time of answering this question.
[Hint: Use pandas.datetime function]


# In[ ]:


The pandas.datetime function is deprecated in recent versions of Pandas. 
Instead, you can use the datetime module in Python's standard library to get the current date and time, 
and then extract the month and year.

Here is an example code snippet that prints the current month and year:


import datetime

# Get the current date and time
now = datetime.datetime.now()

# Extract the month and year
current_month = now.month
current_year = now.year

# Print the current month and year
print(f"Current month: {current_month}")
print(f"Current year: {current_year}")
This code uses the datetime.now() function to get the current date and time, 
and then extracts the month and year using the month and year attributes of the resulting datetime object. 
Finally, it prints the current month and year using formatted strings.

Note that the output of this code will depend on the current date and time when it is executed.




# In[ ]:


Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
calculates the difference between them in days, hours, and minutes using Pandas time delta. The
program should prompt the user to enter the dates and display the result.


# In[ ]:


Here is an example code snippet that takes two dates in the format YYYY-MM-DD as input, 
calculates the difference between them in days, hours, and minutes using Pandas time delta, and displays the result:

import pandas as pd

# Prompt the user to enter the dates
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert the dates to datetime objects
date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)

# Calculate the time difference between the dates
time_diff = date2 - date1

# Extract the number of days, hours, and minutes in the time difference
days = time_diff.days
hours = time_diff.seconds // 3600
minutes = (time_diff.seconds // 60) % 60

# Display the result
print(f"The time difference between {date1} and {date2} is:")
print(f"{days} days, {hours} hours, and {minutes} minutes.")
This code uses the input() function to prompt the user to enter two dates in the format YYYY-MM-DD. 
It then converts the input strings to Pandas datetime objects using the pd.to_datetime() function. 
The time difference between the two dates is calculated using the subtraction operator (-), 
which returns a Pandas Timedelta object.

The code then extracts the number of days, hours, 
and minutes in the time difference using the days attribute and 
the seconds attribute (which is converted to hours and minutes using integer division and modulus operations).
Finally, the result is displayed using formatted strings.




# In[ ]:





# In[ ]:




