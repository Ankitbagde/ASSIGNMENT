#!/usr/bin/env python
# coding: utf-8
# Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.
Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.
# In[10]:


import re

def check_password(password):
    # Check length of password
    if len(password) != 10:
        return "Invalid Password"
    
    # Check for at least 2 uppercase and 2 lowercase letters
    if sum(1 for c in password if c.isupper()) < 2 or sum(1 for c in password if c.islower()) < 2:
        return "Invalid Password"
    
    # Check for at least 1 digit and 3 special characters
    if not re.search(r"\d", password) or not re.search(r"[!@#$%^&*()_+-={}|\\:;\"'<>,.?/]", password) or sum(1 for c in password if re.match(r"[!@#$%^&*()_+-={}|\\:;\"'<>,.?/]", c)) < 3:
        return "Invalid Password"
    
    # Password meets all requirements
    return "Valid Password"


# In[ ]:


Check if the string starts with a particular letterY


# In[9]:


strings = ["apple", "banana", "cherry", "date", "elderberry"]
letter = "c"
result = list(filter(lambda x: x.startswith(letter), strings))
print(result)  # Output: ['cherry']




# In[ ]:





# In[ ]:





# In[ ]:


#1.Check if the string is numericY


# In[8]:


strings = ["123", "3.14", "1e3", "hello", "789"]
result = list(filter(lambda x: x.isnumeric(), strings))
print(result)  # Output: ['123', '789']


# In[ ]:


#2.Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-


# In[7]:


fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]
result = sorted(fruits, key=lambda x: x[1])
print(result)  # Output: [('orange', 80), ('mango', 99), ('grapes', 1000)]


# In[ ]:


#3.Find the squares of numbers from 1 to 10


# In[6]:


result = [i ** 2 for i in range(1, 11)]
print(result)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[ ]:


#4.Find the cube root of numbers from 1 to 10.


# In[5]:


import math

result = list(map(lambda x: math.pow(x, 1/3), range(1, 11)))
print(result)  # Output: [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968, 1.8171205928321397, 1.912931182772389, 2.0, 2.080083823051904, 2.154434690031884]


# In[ ]:


#5.Check if a given number is even.


# In[4]:


number = 17
result = "even" if (lambda x: x % 2 == 0)(number) else "odd"
print(result)  # Output: odd


# In[ ]:


#6.Filter odd numbers from the given list.
[1,2,3,4,5,6,7,8,9,10]


# In[3]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 1, numbers))
print(result)  # Output: [1, 3, 5, 7, 9]


# In[ ]:


#7.Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]


# In[2]:


numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(positive_numbers)  # Output: [1, 2, 3, 4, 5, 6]
print(negative_numbers)  # Output: [-1, -2, -3, -4, -5]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




