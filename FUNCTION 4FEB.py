#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[ ]:


#ANS--Here's a Python program to sort a list of tuples based on integer value using a lambda function:

python code
my_list = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)
#This program uses the sorted() function to sort the list of tuples based on the second element of each tuple (which is an integer).
The key argument is used to specify a lambda function that returns the second element of each tuple. 
The lambda function lambda x: x[1] takes a tuple x as input and returns its second element (which is an integer).


# In[ ]:


Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[ ]:


#ANS Here's a Python program to find the squares of all the numbers in a given list of integers using lambda and map functions:

python code
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, my_list))
print(squares)

#This program uses the map() function to apply a lambda function to each element of the list.
The lambda function lambda x: x**2 takes a number x as input and returns its square. 
The list() function is used to convert the map object to a list.


# In[ ]:


Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


# In[2]:


#Here's a Python program to convert a list of integers into a tuple of strings using map and lambda functions:

#python code
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = tuple(map(lambda x: str(x), my_list))
print(my_tuple)

#This program uses the map() function to apply a lambda function to each element of the list.
#The lambda function lambda x: str(x) takes a number x as input and returns its string representation. 
#The tuple() function is used to convert the map object to a tuple.


# In[ ]:


Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.


# In[ ]:


#Here's a Python program to compute the product of a list containing numbers from 1 to 25 using the reduce() function:

python code
from functools import reduce

my_list = range(1, 26)
product = reduce(lambda x, y: x*y, my_list)
print(product)

#This program uses the reduce() function from the functools module to compute the product of all the numbers in the list.
The lambda function lambda x, y: x*y takes two numbers x and y as input and returns their product. 
The reduce() function applies this lambda function to the first two elements of the list, 
then to the result and the third element, and so on, until all the elements have been processed and a single value (the product) is obtained.


# In[ ]:





# In[ ]:


Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[3]:


#Here's a Python program that filters the numbers in a given list that are divisible by 2 and 3 using the filter function:



numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

result = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

print(result)
#Output:
[6, 60, 90, 120]




# In[ ]:


Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']


# In[4]:


#Here's a Python program that finds palindromes in the given list of strings using lambda and filter function:


words = ['python', 'php', 'aba', 'radar', 'level']

result = list(filter(lambda word: word == word[::-1], words))

print(result)
#Output:

['aba', 'radar', 'level']




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




