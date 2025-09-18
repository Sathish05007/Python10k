
# Before OOP:

# Programming was done mainly in two ways:

# 1. POP (Procedural Oriented Programming)

# Focus is on functions/procedures.
# Data and functions are separate.
# Functions take input → process → return output.
# Example: C language.

# Problems with POP:

# Data is not secure (any function can access/modify it).
# Difficult to manage large projects (too many functions).
# Code reusability is low.



# 2. FOP (Functional Oriented Programming)

# Focus is on mathematical functions.
# Uses concepts like higher-order functions, recursion, immutability.
# Example: Haskell, Lisp, parts of Python.

# Problems with FOP:

# Complex when working with real-world entities.
# No strong way to bind data + behavior together.



# 3. OOP (Object Oriented Programming)

# Focus is on objects (real-world entities).
# Combines data (attributes) and methods (functions) inside a single unit called class/object.
# Provides data security and reusability.
# Example: Python, Java, C++, C#.



#  Python is Multi-Paradigm

# Python supports:

# POP → You can write simple functions.
# FOP → You can use lambda, map, reduce, filter.
# OOP → You can create classes, objects, encapsulation, inheritance.

# So Python gives flexibility to use different paradigms as per requirement.



#  Why OOP? (Main Use: Data Security & Organization)

# 1. Encapsulation (Data Security)

# Data (variables) and code (methods) are kept together.
# By using private/protected/public access specifiers, we can hide sensitive data.
# Example: `__password` in Python class can’t be accessed directly.

# 2. Abstraction

# Hides complex implementation, shows only necessary details.
# Example: When you call `car.start()`, you don’t need to know how the engine works.

# 3. Inheritance

# Reuse code by creating new classes from existing ones.
# Example: `class Car` → `class ElectricCar(Car)`

# 4. Polymorphism

# One interface, multiple implementations.
# Example: `+` operator works for both numbers and strings (`2+3`, `"a"+"b"`).



#  Benefits of OOP

# 1. Data Security → Encapsulation ensures controlled access.
# 2. Code Reusability → Inheritance saves time.
# 3. Modularity → Large projects can be divided into smaller classes.
# 4. Scalability → Easy to maintain and extend.
# 5. Closer to Real-World → Classes and objects map directly to real entities.


# Object-Oriented Programming (OOP) in Python

#  What is OOP?

# Object-Oriented Programming is a programming paradigm where the focus is on creating objects that contain:

#  Data (attributes/variables)
#  Behavior (methods/functions)

# Instead of just writing functions and procedures (like in POP), OOP organizes code into classes & objects, making it more secure, reusable, and easier to manage.



#  Why OOP in Python?

# 1. Data Security (through encapsulation).
# 2. Code Reusability (through inheritance).
# 3. Flexibility (through polymorphism).
# 4. Simplicity (through abstraction).
# 5. Makes it easier to model real-world entities (e.g., Student, Car, Employee).



#  Main OOP Concepts in Python

# 1. Class

#     A blueprint for creating objects.
#     Defines what attributes (data) and methods (functions) an object will have.
#     Example: "Car" is a class.

# 2. Object

#     An instance of a class.
#     Example: "BMW car" is an object of the "Car" class.

# 3. Encapsulation

#     Hiding sensitive data and controlling access.
#     Example: Bank account details hidden from direct access.

# 4. Abstraction

#     Hiding unnecessary details and showing only essential features.
#     Example: Using a mobile phone without knowing the internal circuits.

# 5. Inheritance

#     Reusing existing code by deriving new classes from old ones.
#     Example: ElectricCar inherits properties from Car.

# 6. Polymorphism

#     Ability of the same function/method to behave differently depending on the object.
#     Example: The word “draw” can mean drawing a picture, drawing money, or drawing a card.



#  Types of OOP in Python

# Python supports different types of inheritance (a key OOP concept):

# 1. Single Inheritance → A child class inherits from one parent class.
# 2. Multiple Inheritance → A child class inherits from more than one parent class.
# 3. Multilevel Inheritance → A child class inherits from a parent, and another class inherits from that child (grandchild concept).
# 4. Hierarchical Inheritance → Multiple child classes inherit from the same parent.
# 5. Hybrid Inheritance → Combination of two or more types of inheritance.



#  Advantages of OOP in Python

#  Organizes code into logical structures.
#  Promotes reusability (inheritance).
#  Provides data security (encapsulation).
#  Easy to maintain and extend.
#  Closer to real-world modeling.
