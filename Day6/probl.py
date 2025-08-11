#some examples of control statements
a=20
if(a>0):
    print(f"{a} is postive number")
else:
    print(f"{a} is a negative number")

b=-99
if(b > 0):
    print(f"{b} is positive number")
elif(b<0):
    print(f"{b} is nagitive number")
elif(b == 0):
    print(f"{b} is equal to zero")
else:
    print("you enter a wrong number place enter a number")

age=20
if(age>18):
    print("You are allow vote")
else:
    print("you are not allow to vote")
   

number=int(input("Enter a number"))
if(number%2 == 0):
    print(f"{number} is even number")
else:
    print(f"{number}is odd number")

#6) if statement with bitwise operator
num=8
if(num & 1 == 0):
   print(f"{num} is even number")


a=20
b=25
if(a>b):
    print(f"{a}is big number")
else:
    print(f"{b} is big number")   


# greatest of three numbers 
a=20
b=30
c=13
if(a>b and a>c):
    print(f"a={a}is big number among three numbers")
elif(b>c):
    print(f"b={b}is big number among three numbers")
else:
    print(f"c={c}is big number")


#check the given year is leap year or not
#first check this must divided by 4,not divided by 100 ,it must also divided by 400
year=int(input("Enter a year for check a leap year or not"))
if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")
  

# #traffic light example
color=input("Enter the color of traffic light (red, yellow, green): ").lower()
if(color== "red"):
    print("Stop")
elif(color== "yellow"):
    print("Ready to move")
elif(color== "green"):
    print("Go")
else:
    print("Invalid color")

# Emcet rank
emcet_rank = int(input("Enter your EAMCET rank: "))   #0 to 25000 cmr college, 25001 to 50000 KU, 50001 to 100000 Mallareddy, 100001 to 150000 SCET College, else management
if emcet_rank <= 25000: 
    print("You are eligible for CMR College.")
elif emcet_rank <= 50000 and emcet_rank > 25000:
    print("You are eligible for KU.")
elif emcet_rank <= 100000 and emcet_rank > 50000:
    print("You are eligible for Mallareddy.")   
elif emcet_rank <= 150000 and emcet_rank > 100000:   
    print("You are eligible for SCET College.") 

else:
    print("TRY in Management.")


if(emcet_rank <=25000):
    print("You are eligible for CMR College.")
elif(emcet_rank <= 50000):
    print("You are eligible for KU.")    



#nested if statement
if emcet_rank <= 25000:     
    print("You are eligible for CMR College.")
    if emcet_rank <= 10000:
        print("You are eligible for scholarship in CMR College.")
    else:
        print("You are eligible for CMR College without scholarship.")

#check weather the person is user or admin
 
user_type = input("Enter your user type (user/admin): ").lower()    

if user_type == "admin":
    print("Welcome, Admin!")
    admin_action = input("Do you want to view the dashboard? (yes/no): ").lower()
    if admin_action == "yes":
        print("Displaying admin dashboard...")
    else:
        print("Exiting admin mode.")    
elif user_type == "user":
    print("Welcome, User!")
    user_action = input("Do you want to view your profile? (yes/no): ").lower()
    if user_action == "yes":
        print("Displaying user profile...")
    else:
        print("Exiting user mode.")        

        
#if you know frontend  you become frontend developer
#if you know backend  you become backend developer
#if you know database  you become database developer
# # if you know frontend, backend, and database you become full stack developer

frontend = input("Do you know frontend development? (yes/no): ").lower()
backend = input("Do you know backend development? (yes/no): ").lower()
database = input("Do you know database development? (yes/no): ").lower()

if(frontend == "yes" and backend == "yes" and database == "yes"):
    print("You are a Full Stack Developer.")
elif frontend == "yes":
    print("You are a Frontend Developer.")
elif backend == "yes":
    print("You are a Backend Developer.")
elif database == "yes":
    print("You are a Database Developer.")
else:
    print("join in 10000 coders.")

is_available = True
if(is_available):
    print("Tickets are available for this mathch")
else:
    print("Tickets are not available for this match")

    #check the number is even or odd
num = 10
if num % 2 == 0:    
    print(f"{num},is even")
else:
    print(f"{num},is odd")

    #vote eligibility
age = 18        
if age >= 18:
    print(f"{age},You are eligible to vote")
else:   
    print(f"{age},You are not eligible to vote")   


#5 ternary condition it is similar to if-else condition

is_login=False

print("welcome to dash bord") if is_login else print("place login")
