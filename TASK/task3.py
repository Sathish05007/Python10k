
#1
num = int(input("Enter a number: "))

if num % 2 == 0:
    if num >= 0:
        print(f"The number {num} is even and positive.")
    elif num <= 0:
        print(f"The number {num} is even and negative.")
    else:
        print(f"The number {num} is even and zero.")
else:
    if num >= 0:
        print(f"The number {num} is odd and positive.")
    elif num <= 0:
        print(f"The number {num} is odd and negative.")
    else:
        print(f"The number {num} is odd and zero.")


#2
age=int(input("Enter age: "))
if(age>=0 and age<=12):
    print("You are a Kid")
elif(age>=13 and age<=19):
    print("You are in Teenage")
elif(age>=20 and age<=40):
    print("You are in Young age")
elif(age>=41 and age<=59):
    print("You are in Prime age")
elif(age>=60):
    print("You are a Senior")
else:
    print("Enter a valid age")

#3
subject_1=float(input("Enter s1_Marks: "))
subject_2=float(input("Enter s2_Marks: "))
subject_3=float(input("Enter s3_Marks: "))
subject_4=float(input("Enter s4_Marks: "))
subject_5=float(input("Enter s5_Marks: "))
subject_6=float(input("Enter s6_Marks: "))

print(subject_1,subject_2,subject_3,subject_4,subject_5,subject_6)
total_marks=(subject_1+subject_2+subject_3+subject_4+subject_5+subject_6)
print(total_marks)

average = total_marks / 6
percentage = (total_marks / 600) * 100
print(percentage)

if(percentage>=90 and percentage<=100):
    print("GRADE:-A")
elif(percentage>=80 and percentage<=89):
    print("GRADE:-B")
elif(percentage>=70 and percentage<=79):
    print("GRADE:-C")
elif(percentage>=60 and percentage<=69):
    print("GRADE:-D")
elif(percentage<60):
    print("GRADE:-F")
else:
    print("You are Failed")

   
# #4
s1 = int(input("Enter s1 length: "))
s2 = int(input("Enter s2 length: "))
s3 = int(input("Enter s3 length: "))

# First check: Can these form a triangle?
if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2):
    # Triangle is valid, now check its type
    if s1 == s2 == s3:
        print("It is an Equilateral Triangle")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("The given sides do not form a valid triangle")


5
balance = int(input("Enter your current balance: "))
amount = int(input("Enter amount to withdraw: "))

if amount > balance:
    print("Insufficient balance.")
elif amount % 100 != 0:
    print("Please enter amount in multiples of 100.")
else:
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: ₹{balance}")


6
def greet_user():
    print("Hello! Welcome to the Python Program.")

greet_user()    

7
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
     return "Cannot divide by zero"
    return a / b
def perform_operation():
    print("Choose operation: +, -, *, /")
    op = input("Enter operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if op == '+':
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    elif op == '*':
        print("Result:", multiply(a, b))
    elif op == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")

perform_operation()        


8
def wish_student(name="Student", program="Engineering"):
    print(f"Welcome {name}, Hope you do good in your {program} program.")

wish_student("sagar","MCA")
wish_student()


#9
def future_age(name, age):
    future = age + 10
    print(f"{name}, you will be {future} years old in 2035.")

future_age("sathish", 24)


#10
def display_student_info(name,age,phone,address,email,blood_group):
    print("Student Details:")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Phone Number:{phone}")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"Blood Group:{blood_group}")

display_student_info("sathish",24,8977239316,"1-82 keshanapalli","@gmail.com","A-")
