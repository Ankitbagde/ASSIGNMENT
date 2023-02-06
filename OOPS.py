#!/usr/bin/env python
# coding: utf-8

# # 'OOPS' STAND FOR OBJECT-ORIENTED PROGRAMMING SYSTEM

# In[1]:


a=1


# In[3]:


type(a)


# In[4]:


print(type(a))


# In[ ]:


class pwskills:
    def welcome_msg()


# In[ ]:


Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

Ans-Class and object are fundamental concepts in Object-Oriented Programming (OOP).

A class is a blueprint or template that defines the attributes and behaviors of objects of the same type. 
It specifies what data an object of the class should have and what actions it should be able to perform.

An object, on the other hand, is an instance of a class, created at runtime. 
Each object has its own unique state, represented by its attributes, and behavior, represented by its methods.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        return f'{self.year} {self.make} {self.model}'
In this example, Car is a class that defines the attributes make, model, and year and a method get_details() that returns a string representation of the car's details.

To create objects of the class, you can use the class name followed by parentheses:

python
Copy code
car1 = Car('Toyota', 'Camry', 2020)
car2 = Car('Honda', 'Civic', 2019)
Now car1 and car2 are two different objects of the Car class, each with its own unique state and behavior. You can access their attributes and call their methods using dot notation:

print(car1.make) # Toyota
print(car2.get_details()) # 2019 Honda Civic
In this example, Car is a class that defines a blueprint for creating car objects. 
car1 and car2 are two objects created from the Car class, each with its own unique state and behavior.

This is the basic idea of how classes and objects work in Object-Oriented Programming. 
Classes provide a way to define reusable templates for objects, while objects provide a way to instantiate and manipulate instances of the class.


# In[5]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Creating an instance of the class
my_car = Car("Toyota", "Camry", 2020)

# Calling the display_info method
my_car.display_info()


# In[12]:


class MyClass:
    def __init__(self, value):
        self.value = value
    def print_value(self):
        print(self.value)


# In[17]:


Q2. Name the four pillars of OOPs.

Ans-The four pillars of Object-Oriented Programming (OOP) are:

1.Abstraction: Hides the implementation details and shows only the necessary information to the outside world.

2.Encapsulation: Wraps data and functions within an object, preventing access from the outside world.

3.Inheritance: Enables creation of a new class based on an existing class, inheriting its properties and behaviors.

4.Polymorphism: Enables objects of different classes to be used interchangeably and to respond differently to the same method call.


# In[ ]:


Q3. Explain why the __init__() function is used. Give a suitable example.

Ans-The __init__ method, also known as the constructor method, 
is a special method in Python that is automatically called when an object of a class is created. 
It is used to initialize the attributes of an object and to set the default values for those attributes.

The syntax for the __init__ method is as follows:
class ClassName:
    def __init__(self, param1, param2, ...):
        self.attribute1 = param1
        self.attribute2 = param2
        ...
Here's an example that demonstrates the use of the __init__ method:

class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        
dog1 = Dog("Labrador", "Buddy", 3)
print(dog1.breed)
print(dog1.name)
print(dog1.age)
Output:

Labrador
Buddy
3
In this example, when the Dog object is created, the __init__ method is automatically called and sets the values of the breed, name, and age attributes.





# In[ ]:


get_ipython().set_next_input('Q4. Why self is used in OOPs');get_ipython().run_line_magic('pinfo', 'OOPs')
Ans-In Object-Oriented Programming (OOP), the self keyword is used to refer to the instance of the class that is calling the method. When a method is called on an object, 
the object is passed to the method as the first argument, 
and it is usually referred to as self within the method.

The use of self allows you to access the attributes and methods of the class within the class itself. 
It also helps to avoid naming conflicts between instance variables and local variables in the method. By using self, you can clearly distinguish between instance variables and local variables, which makes your code more readable and maintainable.

Here's an example to demonstrate the use of self:

class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} barks!")
        
dog1 = Dog("Labrador", "Buddy", 3)
dog1.bark()
Output:
Buddy barks!

In this example, self is used to refer to the instance of the Dog class that is calling the bark method. 
The self.name attribute is used to print the name of the dog that is barking.




# In[ ]:


Q5. What is inheritance? Give an example for each type of inheritance.
ANS-Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows you to create new classes based on existing classes. The new class inherits the attributes and behaviors of the existing class, which is referred to as the base class or the superclass.

There are several types of inheritance in OOP, including:

Single inheritance: When a new class is derived from a single base class, it is called single inheritance. 
    The derived class is referred to as the subclass.
Example:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark")
        
dog1 = Dog("Buddy", "Labrador")
dog1.make_sound()
Output:

Bark

In this example, the Dog class is derived from the Animal class, so it inherits the name and species attributes and the make_sound method. 
The Dog class also has a new attribute, breed, and it overrides the make_sound method to print "Bark" instead of "Sound".

Multiple inheritance: When a new class is derived from multiple base classes, it is called multiple inheritance.
Example:


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound")
        
class Domestic:
    def __init__(self, name, is_domestic):
        self.name = name
        self.is_domestic = is_domestic
        
class Dog(Animal, Domestic):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        Domestic.__init__(self, name, is_domestic=True)
        self.breed = breed
        
dog1 = Dog("Buddy", "Labrador")
print(dog1.species)
print(dog1.is_domestic)
Output:

Dog
True
In this example, the Dog class is derived from the Animal and Domestic classes, so it inherits the name, species, and is_domestic attributes.

Multi-level inheritance: When a new class is derived from a derived class, it is called multi-level inheritance.
Example:


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):


