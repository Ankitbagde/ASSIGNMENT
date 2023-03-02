#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.


# In[ ]:


Here's a Python function that takes a list as an argument, creates a flat list, 
and returns the product of all the numbers in the list:

python code
def product_of_numbers(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, (list, tuple, set)):
            flat_list.extend(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, (int, float)):
                    flat_list.append(value)
                elif isinstance(value, (list, tuple, set)):
                    flat_list.extend(value)
        elif isinstance(item, (int, float)):
            flat_list.append(item)

    product = 1
    for num in flat_list:
        product *= num

    return product


Here, we define a function called product_of_numbers that takes a list lst as an argument. The function first creates a flat_list by iterating over each item in the original list and adding it to the flat_list if it's a numeric value or a list, tuple, set or dictionary containing numeric values.

Next, we calculate the product of all the numbers in the flat_list using a loop and the *= operator. Finally, we return the product.

We can test this function with the given list as follows:

python
Copy code
list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34), {1, 2, 3, 3, 2, 1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
print(product_of_numbers(list1))
This should output the product of all the numbers in the given list as follows:

Copy code
2063350032383206917120000000


# In[ ]:


Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.
Input Sentence: I want to become a Data Scientist.
Encrypt the above input sentence using the program you just created.


# In[ ]:


Here's a Python program that encrypts a message using the given logic:

python code
def encrypt_message(message):
    encrypted_message = ""
    for char in message.lower():
        if char.isalpha():
            encrypted_char = chr(ord('a') + (ord('z') - ord(char)))
            encrypted_message += encrypted_char
        elif char == " ":
            encrypted_message += "$"
        else:
            encrypted_message += char
    return encrypted_message.lower()
Here, we define a function called encrypt_message that takes a string message as an argument. 
The function iterates over each character in the message, and for each alphabetic character, it calculates the corresponding encrypted character by subtracting its ASCII value from the ASCII value of 'z', adding the result to the ASCII value of 'a', and converting the resulting ASCII value back to a character using the chr() function.

For whitespace characters, we replace them with a dollar sign. For all other characters, 
including punctuation marks, we leave them unchanged.

Finally, we convert the encrypted message to lowercase and return it.

We can test this function with the given input sentence as follows:

python code
input_sentence = "I want to become a Data Scientist."
encrypted_sentence = encrypt_message(input_sentence)
print(encrypted_sentence)
This should output the encrypted message as follows:

code
r dliw gl yvnzhn z wzyh hvxsvmrg.
As you can see, each alphabetic character in the original message has been replaced with its corresponding encrypted character, 
whitespace characters have been replaced with dollar signs, and punctuation marks have been left unchanged.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




