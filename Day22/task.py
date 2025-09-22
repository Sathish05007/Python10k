# Problem 1
class Animal:
    def sound(self):
        print("Animal: Makes a sound")

class Dog(Animal):
    def speek(self):
        print("Dog: Barks")

dog = Dog()
dog.sound()
dog.speek()

# Problem 2
class Vehicle:
    def start(self):
        print("Vehicle: Starting...")

class Car(Vehicle):
    def drive(self):
        print("Car: Driving...")

car = Car()
car.start()
car.drive()

# Problem 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

sagar = Student("sagar", 25, 101)
sagar.display()

# Problem 4
class Shape:
    def area(self):
        print("Shape: Calculating area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle Area: {3.14 * self.radius * self.radius}")

thing = Circle(5)
thing.area()

# Problem 5
class Employee:
    def basic_salary(self):
        return 30000

class Manager(Employee):
    def bonus(self):
        return 10000

    def total_salary(self):
        print(f"Total Salary: {self.basic_salary() + self.bonus()}")

sagar = Manager()
sagar.total_salary()

# Problem 1
class Organism:
    def who_am_i(self):
        print("I am an organism")

class Animal(Organism):
    def who_am_i(self):
        print("I am an animal")

class Dog(Animal):
    def who_am_i(self):
        print("I am a dog")

d = Dog()
d.who_am_i()

# Problem 2
class Device:
    def show_features(self):
        print("Device: Basic features")

class Laptop(Device):
    def show_features(self):
        print("Laptop: Features")

class GamingLaptop(Laptop):
    def show_features(self):
        print("Gaming Laptop: High-end features")

gl = GamingLaptop()
gl.show_features()

# Problem 3
class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name

class College(University):
    def __init__(self, uni_name, college_name):
        super().__init__(uni_name)
        self.college_name = college_name

class Student(College):
    def __init__(self, uni_name, college_name, student_name):
        super().__init__(uni_name, college_name)
        self.student_name = student_name

    def display(self):
        print(f"University: {self.uni_name}, College: {self.college_name}, Student: {self.student_name}")

s = Student("OU", "Nizam", "Sagar")
s.display()

# Problem 4
class Grandfather:
    def __init__(self):
        self.grandfather_property = 100000

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.father_property = 50000

class Son(Father):
    def __init__(self):
        super().__init__()
        self.son_property = 20000

    def total_inheritance(self):
        print(f"Total Inheritance: {self.grandfather_property + self.father_property + self.son_property}")

s = Son()
s.total_inheritance()

# Problem 5
class Vehicle:
    def __init__(self):
        print("Vehicle: Generic vehicle")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car: Class initialized")

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("Electric Car: Battery powered")

ec = ElectricCar()

# Problem 1
class Employee:
    def work(self):
        print("Employee: Works")

class Manager(Employee):
    def work(self):
        print("Manager: Manages")

class Developer(Employee):
    def work(self):
        print("Developer: Codes")

m = Manager()
m.work()
d = Developer()
d.work()

# Problem 2
class Shape:
    def area(self):
        print("Shape: Area calculation")

class Rectangle(Shape):
    def area(self):
        print("Rectangle: Length * Breadth")

class Triangle(Shape):
    def area(self):
        print("Triangle: 0.5 * Base * Height")

class Circle(Shape):
    def area(self):
        print("Circle: π * r^2")

r = Rectangle()
r.area()
t = Triangle()
t.area()
c = Circle()
c.area()

# Problem 3
class Animal:
    def make_sound(self):
        print("Animal: Makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog: Barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat: Meows")

class Cow(Animal):
    def make_sound(self):
        print("Cow: Moos")

Dog().make_sound()
Cat().make_sound()
Cow().make_sound()

# Problem 4
class Account:
    def login(self):
        print("Account: Login successful")

class SavingsAccount(Account):
    def account_type(self):
        print("Savings Account")

class CurrentAccount(Account):
    def account_type(self):
        print("Current Account")

s = SavingsAccount()
s.login()
s.account_type()

c = CurrentAccount()
c.login()
c.account_type()

# Problem 5
class Appliance:
    def __init__(self, power_rating):
        self.power_rating = power_rating

class Fan(Appliance):
    def consumption(self):
        print(f"Fan: {self.power_rating * 2} units")

class AC(Appliance):
    def consumption(self):
        print(f"AC: {self.power_rating * 10} units")

class Heater(Appliance):
    def consumption(self):
        print(f"Heater: {self.power_rating * 7} units")

fan = Fan(1)
fan.consumption()

ac = AC(2)
ac.consumption()

heater = Heater(3)
heater.consumption()

# Problem 1
class Father:
    def traits(self):
        print("Father: Honest")

class Mother:
    def traits(self):
        print("Mother: Kind")

class Child(Father, Mother):
    def all_traits(self):
        print("Child Inherits:")
        Father.traits(self)
        Mother.traits(self)

c = Child()
c.all_traits()

# Problem 2
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Engineer(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self, salary)

    def show(self):
        print(f"Engineer: {self.name}, Salary: {self.salary}")

eng = Engineer("Sagar", 50000)
eng.show()

# Problem 3
class Flyable:
    def fly(self):
        print("Flyable: Can fly")

class Swimmable:
    def swim(self):
        print("Swimmable: Can swim")

class Duck(Flyable, Swimmable):
    def show(self):
        self.fly()
        self.swim()

duck = Duck()
duck.show()

# Problem 4
class Writer:
    def write(self):
        print("Writer: Writes")

class Singer:
    def sing(self):
        print("Singer: Sings")

class Artist(Writer, Singer):
    def perform(self):
        self.write()
        self.sing()

a = Artist()
a.perform()

# Problem 5
class MathTeacher:
    def teach_math(self):
        print("Math Teacher: Teaches math")

class PhysicsTeacher:
    def teach_physics(self):
        print("Physics Teacher: Teaches physics")

class Tutor(MathTeacher, PhysicsTeacher):
    def teach_all(self):
        self.teach_math()
        self.teach_physics()

t = Tutor()
t.teach_all()

# Problem 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        Person.__init__(self,name)
        self.course = course

class Employee(Person):
    def __init__(self, name, job):
        Person.__init__(self,name)
        self.job = job

class Intern(Student, Employee):
    def __init__(self, name, course, job):
        Student.__init__(self, name, course)
        Employee.__init__(self, name, job)

    def show_profile(self):
        print(f"Intern: {self.name}, Course: {self.course}, Job: {self.job}")

intern = Intern("Sagar", "Python", "Internship")
intern.show_profile()

# Problem 2
class Vehicle:
    def info(self):
        print("Vehicle: Basic info")

class Car(Vehicle):
    def car_info(self):
        print("Car: Has 4 wheels")

class Truck(Vehicle):
    def truck_info(self):
        print("Truck: Heavy vehicle")

class ElectricCar(Car):
    def battery_info(self):
        print("ElectricCar: 400 km range")

e = ElectricCar()
e.info()
e.car_info()
e.battery_info()

# Problem 3
class LivingThing:
    def type(self):
        print("LivingThing: All are alive")

class Animal(LivingThing):
    def move(self):
        print("Animal: Can move")

class Bird(Animal):
    def fly(self):
        print("Bird: Can fly")

class Mammal(Animal):
    def walk(self):
        print("Mammal: Can walk")

class Bat(Bird, Mammal):
    def show(self):
        self.type()
        self.move()
        self.fly()
        self.walk()

bat = Bat()
bat.show()

# Problem 4
class Device:
    def device_info(self):
        print("Device: Basic device")

class Mobile(Device):
    def mobile_info(self):
        print("Mobile: Touch screen")

class Tablet(Device):
    def tablet_info(self):
        print("Tablet: Large screen")

class SmartDevice(Mobile, Tablet):
    def all_features(self):
        self.device_info()
        self.mobile_info()
        self.tablet_info()

sd = SmartDevice()
sd.all_features()
