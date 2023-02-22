#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle.


# In[1]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


# In[ ]:


#Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity.


# In[ ]:


class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity} people."


# In[ ]:


#Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.


# In[ ]:


# Multiple inheritance is a feature of object-oriented programming 
where a class can inherit properties and methods from multiple parent classes. 
In Python, a class can inherit from multiple classes by specifying all parent classes in the class definition.


# In[ ]:


class A:
    def method_A(self):
        print("Method A")
        
class B:
    def method_B(self):
        print("Method B")

class C(A, B):
    def method_C(self):
        print("Method C")

c = C()
c.method_A() # Output: Method A
c.method_B() # Output: Method B
c.method_C() # Output: Method C


# In[ ]:


#Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
class.


# In[ ]:


Getter and setter are methods used to get and set the values of instance variables in a class.
   #Getter is used to get the value of an instance variable,
   while setter is used to set the value of an instance variable.


# In[ ]:


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

p = Person("John", 30)
print(p.get_name()) # Output: John
p.set_name("Peter")
print(p.get_name()) # Output: Peter
print(p.get_age()) # Output: 30
p.set_age(35)
print(p.get_age()) # Output: 35


# In[ ]:


#Q5.What is method overriding in python? Write a python code to demonstrate method overriding.


# In[ ]:


Method overriding is a feature of object-oriented programming 
where a subclass provides its own implementation of a method 
that is already defined in its superclass.
The method in the subclass must have the same name, 
parameters, and return type as the method in the superclass.


# In[ ]:


class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

a = Animal()
a.make_sound() # Output: The animal makes a sound.

c = Cat()
c.make_sound() # Output: Meow


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




