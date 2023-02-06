#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.

Ans-The keyword used to create a function in Python is "def". 
Here's a function to return a list of odd numbers in the range of 1 to 25:


# In[1]:


def odd_numbers():
    odd_list = []
    for i in range(1, 26):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

print(odd_numbers()) #output-[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]


# In[2]:


def odd_numbers(n):
    odd_list = []
    for i in range(1, n+1):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

print(odd_numbers(25))


# In[ ]:


Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
demonstrate their use.

Ans-*args and **kwargs are used in Python to pass a variable number of arguments to a function.

*args allows you to pass a non-keyworded, variable length argument list to a function.
It's defined with an asterisk * before the parameter name and it allows you to pass any number of positional arguments to the function.

**kwargs allows you to pass keyworded, variable length of arguments to a function.
It's defined with two asterisks ** before the parameter name and it allows you to pass any number of keyword arguments to the function.


# In[3]:


def test_function(*args):
    print("This is a test function")
    for arg in args:
        print(arg)
        
def test_kwargs(**kwargs):
    print("This is a test function")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
# *args example
test_function("Hello", "World", 1, 2, 3)

# **kwargs example
test_kwargs(name="John", age=30, city="New York")##This is a test function
Hello
World
1
2
3
This is a test function
name : John
age : 30
city : New York


# In[4]:


def print_args(*args):
    for arg in args:
        print(arg)

print_args("apple", "banana", "cherry") #apple,banana,cherry


# In[5]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(first_name="John", last_name="Doe")#first_name: John
last_name: Doe


# In[ ]:


Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
18, 20].
Ans-An iterator in Python is an object that can be iterated (looped) upon. 
It implements two methods, __iter__() and __next__(),
which allow us to traverse through all the elements of a collection (such as a list).

__iter__ method is used to initialize the iterator object. It returns the iterator object itself.

__next__ method is used for iteration. It returns the next value from the iterator. 
If there are no more items to return, it raises a StopIteration exception.


# In[8]:


class IterateList:
    def __init__(self, list_):
        self.list_ = list_
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list_):
            item = self.list_[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

list_ = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iterable = IterateList(list_)
iterator = iter(iterable)

for i in range(5):
    print(next(iterator))##output-2,4,6,8,10
    


# In[9]:


lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Initialize the iterator
it = iter(lst)

# Use next() method to get the next value
for i in range(5):
    print(next(it))


# In[ ]:


Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.

Ans-A generator function is a special type of function in Python that allows you to return an iterator object. It is defined like a normal function, but instead of using the return keyword, it uses the yield keyword. When the generator function is called, it returns an iterator object, but it does not execute the function's code immediately. The code inside the generator function is executed only when the next() method is called on the iterator.

The yield keyword is used because it allows the function to generate a sequence of values (i.e., a generator), instead of computing them all at once and returning them in a list. This is useful when you want to generate a sequence of values, but don't want to store them all in memory at once.

Here's an example
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):  

    print(num)




# In[ ]:


Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.


# In[13]:


def prime_numbers(n):
    primes = []
    for num in range(2, n):
        for i in primes:
            if (num % i) == 0:
                break
        else:
            primes.append(num)
            yield num

prime_gen = prime_numbers(1000)
for i in range(20):
    print(next(prime_gen))
    #output
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71


# In[ ]:





# In[ ]:





# In[ ]:




