
#MULTI-LEVEL
# class Krishna:
#     def __init__(self):
#         self.krishna_assets = 200
#         print("Krishna's assets are ₹", self.krishna_assets, "Cr")

# class MaheshBabu(Krishna):
#     def __init__(self):
#         super().__init__()
#         self.mahesh_assets = 300
#         print("Mahesh Babu's assets are ₹", self.mahesh_assets, "Cr")

# class Sithara(MaheshBabu):
#     def __init__(self):
#         super().__init__()
#         self.sithara_assets = 100
#         print("Sithara's own assets are ₹", self.sithara_assets, "Cr")

#     def total_assets(self):
#         total = self.krishna_assets + self.mahesh_assets + self.sithara_assets
#         print(f"Total assets including Krishna, Mahesh Babu, and Sithara: ₹{total} Cr")

# s = Sithara()
# s.total_assets()


# class Cherru:
#     def __init__(self):
#         self.cherru_assets = 500
#         print("Cherru's assets are",self.cherru_assets,"Cr")

# class Ram(Cherru):
#     def __init__(self):
#         super().__init__()
#         self.ram_assets = 300
#         print("Ram's Assets are",self.ram_assets,"Cr")

#     def total_assets(self):
#         total = self.cherru_assets + self.ram_assets  
#         print(f"Total assets: {total} Cr")  

# r=Ram()
# r.total_assets()




#Methode overriding --> replacing or changing the logic of methode from superclass in sunclass is called methode overriding
#                   --> It can be applicable only when inheritence happens otherwise it can't work


class Vehicle:
    def speed(self):
        print("vechicle speed is normal")
class Car(Vehicle):
    def speed(self):
        print("Car speed is 120kmph")
class Cycle(Vehicle):
    def speed(self):
        print("Cycle speed is 20kmph")
obj=Car()
obj1=Cycle()    

obj.speed()
obj1.speed()

# class College:
#     st_name="sagar"
#     rank=2000
#     name="ABC Engineering College"
#     loaction="Hyd"
#     fee=50000
# obj1=College()
# print(obj1.st_name,obj1.rank,obj1.name,obj1.loaction,obj1.fee)

# obj1.st_name="sathish ejjagiri"
# print(obj1.st_name,obj1.rank,obj1.name,obj1.loaction,obj1.fee)

# print("")

# class Laptop:
#     brand="Dell"
#     ram="16GB"
#     price="70K"
# c1=Laptop()
# c2=Laptop()
# print(c1.brand,c1.ram,c1.price)
# print(c2.brand,c2.ram,c2.price)   
# c2.brand="HP"
# print(c2.brand,c2.ram,c2.price)   

# print("")

# class Country:
#     name="India"
#     capital="New Delhi"

# c_1=Country()
# c_2=Country()
# c_1.capital="Mumbai"
# print(c_1.name,c_1.capital)
# print(c_2.name,c_2.capital)

# print("")

# class Fan:
#     color="red"
#     blades=3
#     company="usha"
# obj=Fan()
# print(obj.color,obj.blades,obj.company)    

# print("")

# class Language:
#     name="python"
#     type="high-level"
# obj=Language()
# print(obj.name,obj.type)    



# Question 1
# Create a class Student that takes name, roll_no, and branch as parameters in the constructor. Print details for 2 students.

# class Student:
#     def __init__(self,name,roll_no,branch,fee):
#         self.name=name
#         self.roll_no=roll_no
#         self.branch=branch
#         self.fee=fee

#     def info(self):
#         print(f"\n Name : {self.name}")
#         print(f" Roll No : {self.roll_no}")
#         print(f" Branch : {self.branch}")
#         print(f" Fee : {self.fee} ") 

# sagar = Student("Sagar",101,"MCA","40k")
# sathish =Student("Sathish",102,"MCA","45k")
# rahul =Student("Rahul",103,"MCA","40k")

# sagar.info()
# sathish.info()
# rahul.info()


# Question 2
# Create a class Book with dynamic attributes title, author, and price. Create 2 different books and display them using a method show().

# class Book:
#    def __init__(self,title,author,price):
#       self.title=title
#       self.author=author
#       self.price=price

#    def show(self):
#       print(f" \n Title : {self.title}")
#       print(f" Author : {self.author}")
#       print(f" Price : {self.price}")

# py=Book("Python for begr","sagar",200)      
# js=Book("Js for begr","sathish",280)      
# webdev=Book("Full Stack","sagar&sathish",900)

# py.show()
# js.show()
# webdev.show()
         


# 🔹 Question 3
# Write a class Mobile that takes brand, ram, storage, and price. Create 3 objects and print only those whose price is greater than ₹15,000.

# class Mobile:
#     def __init__(self,brand,ram,price):
#         self.brand=brand
#         self.ram=ram
#         self.price=price

#     def info(self):
#         print(f"\n Brand : {self.brand}")
#         print(f" Ram : {self.ram}")
#         print(f" Price : {self.price}")    
# def data():
#  mobiles =[
#  Mobile("Apple",10,16000),
#  Mobile("Poco",6,2000),
#  Mobile("Nokiya",1,1500),
#  Mobile("redme",5,20000),
#  ]
#  for i in mobiles:
 
#   if(i.price > 15000):
#     i.info()
#   else:
#     print(f"\n Brand : {i.brand}")
#     print("The price is Less than 15000")

# data()


# 🔹 Question 4
# Create a class Movie with attributes name, genre, rating. Create a method is_hit() that prints “Hit” if rating > 7 else “Flop”.

# 🔹 Question 5
# Write a class Employee that dynamically stores name, id, and salary. Write a method increment_salary() that increases the salary by ₹5000 and then prints it.



# 🧩 Part 2: Single Inheritance Problems

# 1. Create a base class Person with name and age. Derive a class Employee that adds employee ID and salary. Write a method to display full employee details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Pinfo(self):
        print(f"{self.name} and {self.age}")

class Employee(Person):
    def __init__(self,name,age,ID,salary):
        super().__init__(name,age)
        self.ID=ID
        self.salary=salary

    def info(self):
        print(f" \n Employye Name : {self.name}")
        print(f" Age : {self.age}")      
        print(f" Employye ID : {self.ID}")
        print(f" Salary : {self.salary}") 

sagar=Employee("sagar",25,101,20000)
sagar.info()
                 

# 2. Create a base class Shape, and a derived class Circle that inherits from Shape. Add radius and method to calculate area of the circle.


# 3. Create a class Vehicle with method start() and stop(). Create a subclass Bike that adds gear_count and overrides the start() method to display a bike-specific message.
