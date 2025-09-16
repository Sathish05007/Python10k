# #Function is a reusable of block of code that execute on calling
# #Parameters are the values that are passed to the function when it is called
# #arguments are the values that are passed to the function when it is called
# #Function without parameter
def function_name():
    #Function body
    a=20
    b=30
    print(a+b)
#Function calling
function_name()
function_name()
function_name()

def wish(name):
    print(f"{name}")
    return "good night"
print(wish("sagar"))


print("=======================")
#Function with parameter
def function_with_parameter(a, b):
    #Function body
    print(a-b)  
#Function calling
function_with_parameter(10, 20)
function_with_parameter(100, 50)
print("=======================")

def wish(name, place):
    print(f"My name is {name} and I am from {place}")

wish("sagar", "Ramagundam")
wish("rahul","Hyderabad")

print("=======================")

# def password(name, password):
#     print(f"Your name is {name} and Yours password is {password}")

# password("sagar","77$9&@")  
print("=======================")  

# #positional arguments
# def positional_arguments(name, place):
#     print(f"My name is {name} and I am from {place}")

# positional_arguments("sagar", "Ramagundam")
# positional_arguments("akhil", "Mulugu")
print("=======================")
# #keyword arguments
# def keyword_arguments(name, place):
#     print(f"My name is {name} and I am from {place}")   

# keyword_arguments(place="Keshanapalli", name="laddu")
# keyword_arguments(name="akhil", place="Mulugu")
print("=======================")

# #default arguments
# def default_arguments(name, batch="53r"):
#     print(f"My name is {name} and I am from {batch} batch")
    
# default_arguments("sagar")
# default_arguments("akhil", "54q") #we can change the default value by passing a new value
print("=======================")


# def items(name, quantity, price=50000):
#     print(f"The item name is: {name}, quantity is: {quantity}, and price is: {price}")

# items("Laptop", 2) #positional argument, price will take default value
# items(quantity=3,name="iphone",price=200000) #keyword argument, price will take the value passed


# #find even or add by using function
# def find_even_or_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is an even number")
#     else:
#         print(f"{number} is an odd number")

# find_even_or_odd(10)    
# find_even_or_odd(15)    
# find_even_or_odd(999)

# print("-------------------------------------------------------")
# def find_positive_nagative(num):
#     if (num>0):
#         print(f"{num} is positive number")
#     else:
#         print(f"{num} is nagetive number") 

# find_positive_nagative(20)
# find_positive_nagative(-88)        

def is_prime(n):
    if (n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print(f"{n} Not a prime number")
    else:
        print(f"{n} Prime number")

# Example
is_prime(2)   # Prime number
is_prime(9)   # Not a prime number
is_prime(13)  # Prime number
is_prime(53)



#max,phy,chem inthis subjects if got above 35 print pass else fail by using if else statement
def check_pass_fail(max_marks, phy_marks, chem_marks):
    if max_marks >= 35 and phy_marks >= 35 and chem_marks >= 35:
        print("You have passed in all subjects.")
    else:
        print("You have failed in one or more subjects.")

check_pass_fail(40, 50, 60)  # Example where all marks are above 35
check_pass_fail(30, 40, 50)  # Example where max_marks is below 35 

#if any two subjects are above 35 print pass else fail
def check_pass_fail_two_subjects(max_marks, phy_marks, chem_marks):
    if (max_marks >= 35 and phy_marks >= 35) or (phy_marks >= 35 and chem_marks >= 35) or (max_marks >= 35 and chem_marks >= 35):
        print("You have passed in at least two subjects.")
    else:
        print("You have failed in two or more subjects.")
check_pass_fail_two_subjects(20, 50, 50)  # Example where two subjects are above 35
check_pass_fail_two_subjects(50, 20, 50)  # Example where max_marks is above 35
check_pass_fail_two_subjects(50, 50, 20)  # Example where all subjects are below 35

# in a money find how many 1000,500,remaining
def find_notes(amount):
    notes_1000 = amount // 1000
    # print(notes_1000) 
    remaining = amount % 1000
    # print(remaining)
    notes_500 = remaining // 500
    # print(notes_500)
    remaining = remaining % 500
    print(f"1000 notes: {notes_1000}, 500 notes: {notes_500}, Remaining: {remaining}")

find_notes(4500)
find_notes(12000)
find_notes(7500)    
find_notes(10000)


amount=5725
notes_1000 = amount // 1000
rem_change= amount-(notes_1000*1000)
notes_500 = rem_change // 500
rem_change = rem_change - (notes_500 * 500)
print(f"1000 notes: {notes_1000}, 500 notes: {notes_500}, Remaining: {rem_change}")

# biggest of three numbers 
def find_biggest_of_three(a, b, c):
    if (a >= b and a >= c):
        print(f"{a} is the biggest number")
    elif (b >= a and b >= c):
        print(f"{b} is the biggest number")
    else:
        print( f"{c} is the biggest number")
# Example
find_biggest_of_three(110, 202, 308)  # Output: 30 is the biggest number

#in a car limite is 5 people write code for 5,10,22,37 people find how may cars are needed
def calculate_cars_needed(people):
    car_capacity = 5
    cars_needed = people // car_capacity
    if (people % car_capacity != 0):
        cars_needed += 1  # Add an extra car for remaining people
    return cars_needed
# Example
print(f"Cars needed for 5 people: {calculate_cars_needed(5)}")
print(f"Cars needed for 10 people: {calculate_cars_needed(10)}")
print(f"Cars needed for 22 people: {calculate_cars_needed(22)}")
print(f"Cars needed for 37 people: {calculate_cars_needed(37)}")
print(f"Cars needed for 370 people: {calculate_cars_needed(370)}")


# perfect square or not
def is_perfect_square(n):   
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n
# Example
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(225))  # Output: False

print(is_perfect_square(300))  # Output: True




def add():
    print(2+3)
    add()
add()    


# Lambda function
# function without function name we called as anonymous 
# dont use def key word,no need of function name,dont gave () ,dont use return key word

sagar= lambda: "hello"
print(sagar) #it prints the function expression only
print(sagar()) #it prints the output


# use lambda key word ,assin this function to a varible,then print the varible and call the function
sagar_1=lambda:print(5)
print(sagar_1())


# with argrments lambda function

sample=lambda x:x*10
print(sample(4))

demo=lambda x,y,z:x+y+z
print(demo(20,30,40))

# name=lambda st_name,address,age,cource:st_name , address , age , cource
# print(name())

name = lambda st_name, address, age, course: [st_name, address, age, course]
print(name("Sathish", "Warangal", 23, "MCA"))
print(name("Warangal", 23, "MCA","sagar"))
print(name(address="Warangal",st_name="sagar", age=23, course="MCA"))



# callback function(high function) combo is known as 1st class function