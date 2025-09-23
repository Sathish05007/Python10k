#Method Overriding (5 Examples)

# Problem 1: Animal Sound
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()

# Problem 2: Vehicle Type
class Vehicle:
    def fuel_type(self):
        print("Generic vehicle fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Car runs on petrol")

v = Vehicle()
v.fuel_type()

c = Car()
c.fuel_type()

# Problem 3: Employee Salary
class Employee:
    def salary(self):
        print("Employee gets base salary")

class Manager(Employee):
    def salary(self):
        print("Manager gets salary + bonus")

e = Employee()
e.salary()

m = Manager()
m.salary()

# Problem 4: Shape Area
class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def area(self):
        print("Area = π * r^2")

s = Shape()
s.area()

c = Circle()
c.area()

# Problem 5: Bank Interest
class Bank:
    def interest_rate(self):
        print("Bank interest rate: 4%")

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate: 5.5%")

b = Bank()
b.interest_rate()

sbi = SBI()
sbi.interest_rate()

#Encapsulation (5 Examples)

#Problem 1: Private Variable

class Person:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        print(f"Name is: {self.__name}")

p = Person("Sagar")
p.get_name()

#Problem 2: Bank Balance
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def get_balance(self):
        print(f"Current Balance: {self.__balance}")

acc = BankAccount()
acc.deposit(500)
acc.get_balance()

# Problem 3: Student Grade
class Student:
    def __init__(self):
        self.__grade = 'A'

    def show_grade(self):
        print(f"Student Grade: {self.__grade}")

s = Student()
s.show_grade()

# Problem 4: Encapsulated Age
class Employee:
    def __init__(self):
        self.__age = 25

    def get_age(self):
        print(f"Age: {self.__age}")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print("Age updated")
        else:
            print("Invalid age")

e = Employee()
e.get_age()
e.set_age(30)
e.get_age()

# Problem 5: Encapsulation with Validation
class Product:
    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        if price > 0:
            self.__price = price
            print("Price updated")
        else:
            print("Invalid price")

    def get_price(self):
        print(f"Product Price: {self.__price}")

p = Product()
p.set_price(150)
p.get_price()

