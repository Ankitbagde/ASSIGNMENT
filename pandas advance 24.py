#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. List any five functions of the pandas library with execution.


# In[ ]:


Function 1: read_csv()

This function is used to read data from a CSV file and create a DataFrame object. Here's an example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
Function 2: head()

This function is used to display the first n rows of a DataFrame. Here's an example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
df.head(10)  # displays the first 10 rows of the DataFrame
Function 3: drop()

This function is used to drop rows or columns from a DataFrame. Here's an example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
df = df.drop(['column1', 'column2'], axis=1)  # drops columns named 'column1' and 'column2'
Function 4: groupby()

This function is used to group the rows of a DataFrame based on the values of one or more columns. Here's an example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
grouped = df.groupby('column1')  # groups the rows of the DataFrame by the values in 'column1'
Function 5: pivot_table()

This function is used to create a pivot table from a DataFrame. Here's an example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
pivot_table = pd.pivot_table(df, values='column1', index=['column2'], columns=


# In[ ]:


Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
DataFrame with a new index that starts from 1 and increments by 2 for each row.


# In[ ]:


Python function to re-index a DataFrame:

python code
import pandas as pd

def reindex_dataframe(df):
    new_index = pd.Index(range(1, len(df)*2, 2))
    new_df = df.set_index(new_index)
    return new_df
This function takes a DataFrame object as input, creates a new index using the range() function,
and sets the new index for the DataFrame using the set_index() method. 
It then returns the new DataFrame with the updated index.


# In[ ]:


Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console.
For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
calculate and print the sum of the first three values, which is 60.


# In[ ]:


Python function to calculate the sum of the first three values in a column:

python code
import pandas as pd

def calculate_sum(df):
   values = df['Values'][:3]
   sum_of_values = sum(values)
   print(sum_of_values)
This function takes a DataFrame object as input,
selects the first three values in the 'Values' column using slicing, calculates their sum using the sum() function,
and prints the result to the console.


# In[ ]:


Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column.


# In[ ]:


Python function to count the number of words in a column and create a new column:

import pandas as pd

def count_words(df):
    word_counts = df['Text'].apply(lambda x: len(x.split()))
    df['Word_Count'] = word_counts
    return df
This function takes a DataFrame object as input, applies a lambda function to count the number of words in each row of the 'Text' column,
and creates a new column called 'Word_Count' with the resulting word counts. It then returns the updated DataFrame.


# In[ ]:


get_ipython().set_next_input('Q5. How are DataFrame.size() and DataFrame.shape() different');get_ipython().run_line_magic('pinfo', 'different')


# In[ ]:


Difference between DataFrame.size() and DataFrame.shape():

DataFrame.size() returns the total number of elements in a DataFrame, i.e., the product of the number of rows and columns. For example:

python code
import pandas as pd
df = pd.read_csv('file.csv')
print(df.size)
DataFrame.shape() returns a tuple containing the number of rows and columns in a DataFrame. For example:

python code
import pandas as pd
df = pd.read_csv('file.csv')


# In[ ]:


get_ipython().set_next_input('Q6. Which function of pandas do we use to read an excel file');get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


The function of pandas used to read an excel file is read_excel(). Here's an example:

python code
import pandas as pd
df = pd.read_excel('file.xlsx')
This function reads data from an Excel file and creates a DataFrame object.


# In[ ]:


Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
addresses in the format 'username@domain.com'. Write a Python function that creates a new column
'Username' in df that contains only the username part of each email address.
The username is the part of the email address that appears before the '@' symbol. For example, if the
email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your
function should extract the username from each email address and store it in the new 'Username'
column.


# In[ ]:


Python function to extract usernames from email addresses and create a new column:

python code
import pandas as pd

def extract_username(df):
    usernames = df['Email'].apply(lambda x: x.split('@')[0])
    df['Username'] = usernames
    return df
This function takes a DataFrame object as input, 
applies a lambda function to extract the username part of each email address in the 'Email' column using the split() method,
and creates a new column called 'Username' with the resulting usernames. It then returns the updated DataFrame.


# In[ ]:


Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
function should return a new DataFrame that contains only the selected rows.
For example, if df contains the following values:
A B C
0 3 5 1
1 8 2 7
2 6 9 4
3 2 3 5
4 9 1 2


# In[ ]:


Here's a Python function that selects rows from a Pandas DataFrame based on two conditions:

python code
import pandas as pd

def select_rows(df):
    # Select rows where A > 5 and B < 10
    mask = (df['A'] > 5) & (df['B'] < 10)
    # Create a new DataFrame with only the selected rows
    selected_rows = df.loc[mask]
    return selected_rows
This function takes a DataFrame object as input and applies a boolean mask to select rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. It then creates a new DataFrame with only the selected rows and returns it. The loc function is used to select rows based on a boolean mask. The & operator is used to combine two conditions.





# In[ ]:




