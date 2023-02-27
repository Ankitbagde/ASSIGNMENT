#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)


# In[ ]:


Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
to print the data types of both the variables.


# In[3]:


#Yes, there is a difference in the data type of variables list_ and array_list. list_ is a Python list of strings, 
#while array_list is a NumPy array of strings.

#To print the data types of both variables, you can use the type() function:
import numpy as np
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print(type(list_))
print(type(array_list))




# In[ ]:


Q2. Write a code to print the data type of each and every element of both the variables list_ and
arra_list.


# In[ ]:


To print the data type of each and every element of both variables, you can use a loop to iterate over the elements and print the type of each element. For example:

python code
import numpy as np
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

# Print data type of elements in list_
for element in list_:
    print(type(element))

# Print data type of elements in array_list
for element in array_list:
    print(type(element))
This will output:

python code
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'numpy.str_'>
<class 'numpy.str_'>
<class 'numpy.str_'>
<class 'numpy.str_'>
<class 'numpy.str_'>




# In[ ]:


Q3. Considering the following changes in the variable, array_list:
array_list = np.array(object = list_, dtype = int)
Will there be any difference in the data type of the elements present in both the variables, list_ and
arra_list? If so then print the data types of each and every element present in both the variables, list_
and arra_list.


# In[ ]:


Yes, there will be a difference in the data type of the elements present in both the variables list_ and array_list, 
because in the original array_list variable the elements were of string data type,
but after changing the dtype to int, the elements will be of integer data type.

To print the data type of each and every element present in both the variables list_ and array_list,
you can use a loop to iterate over the elements and print the type of each element. For example:

python code
import numpy as np
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_, dtype=int)

# Print data type of elements in list_
for element in list_:
    print(type(element))

# Print data type of elements in array_list
for element in array_list:
    print(type(element))
This will output:

python
Copy code
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'numpy.int64'>
<class 'numpy.int64'>
<class 'numpy.int64'>
<class 'numpy.int64'>
<class 'numpy.int64'>
As you can see, the data type of the elements in list_ is str,
while the data type of the elements in array_list is numpy.int64


# In[ ]:


Consider the below code to answer further questions:
import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)
Q4. Write a code to find the following characteristics of variable, num_array:
(i) shape
(ii) size


# In[ ]:


To find the shape and size of the variable num_array, 
   you can use the shape and size attributes of the NumPy array. For example:

python code
import numpy as np
num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)

# Find shape of num_array
print(num_array.shape)

# Find size of num_array
print(num_array.size)
This will output:

(2, 3)
6
The shape attribute gives the dimensions of the NumPy array, which in this case is a 2x3 matrix, 
and the size attribute gives the total number of elements in the NumPy array, which is 6.


# In[ ]:


Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
creation function.
[Hint: The size of the array will be 9 and the shape will be (3,3).]


# In[4]:


#To create a NumPy array of a 3x3 matrix containing only zeros, you can use the zeros() function from NumPy. 
  # For example:

import numpy as np

# Create array of zeros with shape (3, 3)
zeros_array = np.zeros((3, 3))

print(zeros_array)



# In[ ]:


get_ipython().set_next_input('Q6. Create an identity matrix of shape (5,5) using numpy functions');get_ipython().run_line_magic('pinfo', 'functions')
[Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]


# In[ ]:


To create an identity matrix of shape (5,5) using NumPy, you can use 
the eye() function and specify the size of the identity matrix as the argument. For example:

python code
import numpy as np

# Create identity matrix with shape (5, 5)
identity_matrix = np.eye(5)

print(identity_matrix)
This will output:

Copy code
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
As you can see, an identity matrix is a square matrix with ones on the diagonal and zeros elsewhere.


# In[ ]:




