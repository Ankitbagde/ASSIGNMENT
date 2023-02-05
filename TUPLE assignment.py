#!/usr/bin/env python
# coding: utf-8

# # TUPLE SET AND DICT ASSIGNMENT:-
# 
# 
# Q1.What are the characteristics of the tuples? Is tuple immutable?
# 
# Ans- Tuples are one of the data structures in Python and have the following characteristics:
# 
# a)Ordered: The elements in a tuple have a defined order and can be accessed by their index.
# 
# b)Immutable: Once a tuple is created, its elements cannot be changed, added, or removed. Tuples are considered immutable objects.
# 
# c)Heterogeneous: Tuples can contain elements of different data types, such as integers, strings, or other objects.
# 
# d)Iterable: Tuples can be iterated over, which means you can access each element in a tuple one by one.
# 
# e)Hashable: Tuples can be used as keys in dictionaries, as long as their elements are hashable.
# 
# In conclusion, yes, tuples are immutable in Python.
# 
# 
# Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why
# tuples have only two in-built methods as compared to Lists.
# 
# Ans-There are two built-in methods in Python for tuples:
# 
# 1- count(): This method returns the number of times a specified value appears in a tuple.
# For example:
# t = (1, 2, 3, 2, 4, 2)
# print(t.count(2)) # Output: 3
# 2-index(): This method returns the index of the first occurrence of a specified value in a tuple. 
# For example:
# t = (1, 2, 3, 4, 5)
# print(t.index(3)) # Output: 2
# 
# Tuples have only two built-in methods because they are designed to be lightweight and efficient data structures for representing simple collections of values. 
# Lists have many more methods, because they are meant to be more flexible and powerful data structures that can be used for more complex tasks. Tuples are intended to be used for small, fixed collections of values that don't need to be modified.
# 

# In[8]:


#Q3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove
duplicates from the given list.
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]

Ans- The set datatype in Python does not allow duplicate items. You can use a set to remove duplicates from a list as follows:
    #List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]


The set constructor is used to create a set from a list, and the duplicates are automatically removed. The resulting set is then converted back to a list using the list constructor. This code will give you a new list with only unique items from the original list


# In[3]:


List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]

# Convert the list to a set and then back to a list
List = list(set(List))

print(List) # Output: [1, 2, 3, 4]


# In[ ]:


Q4. Explain the difference between the union() and update() methods for a set. Give an example of
each method.

Ans-The union and update methods are used to merge two sets in Python. 
However, there is a difference between the two methods in how they merge the sets:


# In[17]:


#union(): This method returns a set that contains all the elements from both sets, without modifying either set.
#For example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result) # Output: {1, 2, 3, 4, 5}
print(set1) # Output: {1, 2, 3}
print(set2) # Output: {3, 4, 5}


# In[20]:


# update(): This method adds all the elements from one set to another set, modifying the set that the method was called on. 
#For example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)

print(set1) # Output: {1, 2, 3, 4, 5}
print(set2) # Output: {3, 4, 5}

#In this example, the update method adds all the elements from set2 to set1, and set1 is modified. 
#However, set2 remains unchanged. The union method, on the other hand, returns a new set that is the combination of both sets, without modifying either set.



# In[ ]:


Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.

Ans-A dictionary in Python is an unordered collection of key-value pairs, where each key maps to a value. A key in a dictionary must be unique and can be used to access its corresponding value. The values can be of any data type and do not have to be unique.

An example of a dictionary in Python is:


In this example, the dictionary person has three key-value pairs: 'name' maps to 'John Doe', 'age' maps to 30, and 'address' maps to '123 Main St'.

Dictionaries are unordered, meaning that the elements in a dictionary do not have a specific order. The order of elements in a dictionary may change when the dictionary is modified, but there is no guaranteed order for the elements in a dictionary.


# In[21]:


person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St'}

print(person['name']) # Output: 'John Doe'
print(person['age']) # Output: 30
print(person['address']) # Output: '123 Main St'


# In[ ]:


Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level
nested dictionary.

Ans-Yes, you can create a nested dictionary in Python. 
A nested dictionary is a dictionary that contains another dictionary as one of its values.

Here's an example of a simple one-level nested dictionary:In this example, the dictionary employees has two key-value pairs.
The value of each key is another dictionary that contains information about an employee.
The nested dictionaries have keys 'name', 'age', and 'address' which map to values for each employee.



# In[22]:


employees = {'employee1': {'name': 'John Doe', 'age': 30, 'address': '123 Main St'},
             'employee2': {'name': 'Jane Doe', 'age': 28, 'address': '456 Main St'}}

print(employees['employee1']) # Output: {'name': 'John Doe', 'age': 30, 'address': '123 Main St'}
print(employees['employee2']['name']) # Output: 'Jane Doe'


# In[ ]:


Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of
the key as this list ['Python', 'Machine Learning’, 'Deep Learning']
dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}


# In[23]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', []).extend(['Python', 'Machine Learning', 'Deep Learning'])

print(dict1) # Output: {'language': 'Python', 'course': 'Data Science Masters', 'topics': ['Python', 'Machine Learning', 'Deep Learning']}


# In[ ]:


Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display
these three view objects for the given dictionary.
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

Ans-There are three view objects in dictionaries in Python: keys(), values(), and items().

The keys() method returns a view object that displays a list of all the keys in the dictionary.
The values() method returns a view object that displays a list of all the values in the dictionary.
The items() method returns a view object that displays a list of all the key-value pairs in the dictionary.


In this example, the keys(), values(), and items() methods are used to display the contents of the dictionary dict1. 
The output of each method shows the view object that contains the keys, values, and key-value pairs, respectively.


# In[24]:


dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

print(dict1.keys())   # Output: dict_keys(['Sport', 'Teams'])
print(dict1.values())  # Output: dict_values(['Cricket', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']])
print(dict1.items())  # Output: dict_items([('Sport', 'Cricket'), ('Teams', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand'])])


# In[ ]:




