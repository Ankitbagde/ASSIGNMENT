#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. What is an Exception in Python? Write the difference between Exceptions and Syntax errors.


# In[ ]:


ANS-In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of 
the program's instructions. Exceptions are raised whenever an error or unexpected condition is encountered while
executing a code block.

Syntax errors, on the other hand, occur when there is an error in the code's syntax. These errors prevent the program
from running at all and are detected during the parsing stage, before the code is actually executed.

The main difference between exceptions and syntax errors is that exceptions are runtime errors that occur during 
program execution, while syntax errors are detected during the parsing stage, before the code is executed.
Additionally, while syntax errors are usually caused by a typo or syntax mistake, exceptions can be caused
by a variety of factors such as invalid input, I/O errors, and other runtime conditions.


# In[ ]:


Q2. What happens when an exception is not handled? Explain with an example.


# In[ ]:


ANS-If an exception is not handled, it will cause the program to terminate abruptly,
and an error message will be displayed. For example, consider the following code:

try:
    x = 10/0
except ValueError:
    print("ValueError occurred")
This code will cause a ZeroDivisionError because we are trying to divide a number by zero. 
If the exception is not handled, the program will terminate and display the error message:
ZeroDivisionError: division by zero


# In[ ]:


Q3. Which Python statements are used to try, catch, and handle exceptions? Explain with an example.


# In[ ]:


ANS-Python provides the following statements to handle exceptions:

try: This statement is used to enclose the code that may raise an exception.

except: This statement is used to handle the exception. 
    It can be followed by one or more exception types that the handler will catch.

finally: This statement is used to execute a block of code regardless of whether an exception occurred or not.

For example, consider the following code:

python code
try:
    x = int(input("Enter a number: "))
    y = 10/x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", y)
finally:
    print("End of program")
In this code, we are trying to divide 10 by the user input. 
If the user enters an invalid input or if we try to divide by zero, 
the corresponding exception will be caught by the appropriate except block. 
If no exception occurs, the else block will be executed, and finally, the finally block will always be executed.



# In[ ]:


Q4. Explain with an example: try and except, finally, raise.


# In[ ]:


ANS-The try and except statements are used to catch and handle exceptions in Python. 
The try block contains the code that may raise an exception, while the except block contains the code that will handle the exception. 
If an exception is raised, the code in the try block will stop executing, and the code in the except block will be executed instead.

For example:
python code
try:
    x = 10/0
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result is:", x)
finally:
    print("The end")
In this example, we are trying to divide 10 by zero, which will raise a ZeroDivisionError.
The except block catches this exception and prints an error message. 
The else block is not executed because an exception occurred,
and the finally block is always executed, printing "The end" to the console


# In[ ]:


Q5. What are Custom Exceptions in Python? Why do we need Custom Exceptions? Explain with an example.


# In[ ]:


ANS-Custom exceptions are user-defined exceptions that can be created 
to handle specific errors that are not covered by the built-in Python exceptions. 
Custom exceptions are created by defining a new exception class that inherits from the base Exception class.

Custom exceptions can be useful in situations where we need to handle specific types of errors that are not covered by the built-in exceptions.
For example, suppose we are building a file management system, and we want to raise an exception when a file with the same name already exists. 
We can create a custom FileAlreadyExistsError exception to handle this case.


# In[ ]:


Q6. Create a Custom Exception class. Use this class to handle an exception.


# In[ ]:


ANS-here's an example of creating a custom exception class and using it to handle an exception:

python code
class NegativeNumberError(Exception):
    pass

def calculate_square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate the square root of a negative number")
    else:
        return num ** 0.5

try:
    result = calculate_square_root(-9)
except NegativeNumberError as e:
    print(e)
else:
    print(result)
In this example, we create a custom exception class called NegativeNumberError.
This class inherits from the built-in Exception class, which allows us to raise and handle this exception just like any other exception in Python.

We then define a function called calculate_square_root that takes a number as an argument and calculates its square root. 
If the number is negative, we raise a NegativeNumberError with a custom error message.

In the try block, we call the calculate_square_root function with a negative number.
Since this will raise a NegativeNumberError, we catch it in the except block and print out the error message. 
If the function was successful, we print out the result.

This is just a simple example, but it shows how we can create and use custom exceptions to handle specific error conditions in our programs.


# In[ ]:




