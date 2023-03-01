#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Explain why we have to use the Exception class while creating a Custom Exception.
Note: Here Exception class refers to the base class for all the exceptions.


# In[ ]:


ANS--In Python, all exceptions are subclasses of the base class Exception. 
When we create a custom exception, we need to create a subclass of Exception 
so that our custom exception inherits all the properties and behaviors of the base class.

By inheriting from the Exception class, our custom exception can be treated
in the same way as the built-in exceptions. This means that our custom exception 
can be caught using the same try-except block that is used to catch built-in exceptions.

In addition, inheriting from the Exception class allows us to define our own custom attributes 
and methods for our exception, while still retaining the common properties shared by all exceptions in Python.

Therefore, using the Exception class as the base class while creating 
a custom exception ensures that our custom exception is fully compatible 
with the Python exception hierarchy and can be handled in a consistent and predictable manner.


# In[ ]:


Q2. Write a python program to print Python Exception Hierarchy.


# In[ ]:


python code
def print_exception_hierarchy():
    """
    Prints the Python Exception Hierarchy, starting from BaseException.
    """
    exceptions = []
    exc = BaseException
    while exc:
        exceptions.append(exc)
        exc = exc.__base__

    for exc in reversed(exceptions):
        print(exc.__name__)
This program defines a function called print_exception_hierarchy that uses a loop to traverse 
the exception hierarchy, starting from BaseException and working its way down 
to the most specific exception classes. The function then prints out the name of each exception class, in order.


# In[ ]:


Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.


# In[ ]:


The ArithmeticError class is a base class for all errors that occur during arithmetic operations.
It has several subclasses, including:

ZeroDivisionError: Raised when dividing a number by zero.
OverflowError: Raised when the result of an arithmetic operation is too large to be represented.
Here are some examples of how these exceptions can be raised:

python code
# ZeroDivisionError
x = 5 / 0  # Raises ZeroDivisionError: division by zero

# OverflowError
x = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
y = x * x  # Raises OverflowError: int too large to convert to float


# In[ ]:


Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.


# In[ ]:


The LookupError class is a base class for all errors that occur when a key or index is not found in a container. 
It has several subclasses, including:

KeyError: Raised when a dictionary key is not found.
IndexError: Raised when trying to access an index that is out of range.
Here are some examples of how these exceptions can be raised:

python code
# KeyError
d = {"foo": 42}
x = d["bar"]  # Raises KeyError: 'bar'

# IndexError
l = [1, 2, 3]
x = l[3]  # Raises IndexError: list index out of range


# In[ ]:


get_ipython().set_next_input('Q5. Explain ImportError. What is ModuleNotFoundError');get_ipython().run_line_magic('pinfo', 'ModuleNotFoundError')


# In[ ]:


ImportError is raised when an imported module or its attributes cannot be found. 
This can happen if the module does not exist, or if there is an error in 
the import statement or in the module itself.

In Python 3.6 and later versions, ModuleNotFoundError is a subclass of ImportError. 
It is raised when the requested module cannot be found in the search path.

Here's an example of how these exceptions can be raised:

python code
# ImportError
import non_existent_module  # Raises ImportError: No module named 'non_existent_module'

# ModuleNotFoundError
import non_existent_module  # Raises ModuleNotFoundError: No module named 'non


# In[ ]:


Q6. List down some best practices for exception handling in python.


# In[ ]:


Here are some best practices for exception handling in Python:

Catch only the exceptions that you can handle: While using a try-except block, it is important to catch only the exceptions that you can handle. 
    Catching all exceptions with a generic except clause can mask bugs in the code and make it difficult to diagnose the root cause of the issue.

Use multiple except blocks: When using a try-except block, 
    it is best practice to use multiple except blocks for handling different exceptions.
    This ensures that each type of exception is handled in a specific way, improving code clarity and making it easier to maintain.

Avoid using bare except clauses: It is generally not a good idea to use bare except clauses,
    as this can catch all types of exceptions, including ones that you might not expect.
    Instead, use specific exception types to catch the errors you need to handle.

Use finally to clean up resources: The finally block is used to execute code regardless of
    whether an exception occurred or not. This is useful for cleaning up resources, such as closing files or releasing network connections.

Raise exceptions with informative messages: When raising exceptions, 
    it is important to provide informative error messages that explain what went wrong and how to fix it. This helps the user to understand the issue and take appropriate action.

Don't ignore exceptions: Ignoring exceptions can hide bugs and make it difficult to diagnose issues.
Even if you don't know how to handle an exception, it is better to log the error message or raise it further up the call stack.

Use context managers: Python's context manager protocol (with statement)
    provides a convenient way to manage resources such as files and network connections.
    By using context managers, you can ensure that resources are properly cleaned up, even if an exception occurs.

By following these best practices, you can write more robust and maintainable code that handles exceptions gracefully and provides informative error messages to the user.


# In[ ]:





# In[ ]:




