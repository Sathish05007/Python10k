# print a number in a rev order with out convert into sting

num=int(input("Enter a number: "))

while(num >0):
    last_digt=(num%10) 
    print(last_digt)
    num=num//10

print(num)

# write above code by using string



# sum of given number with out convert in to string
num=int(input("Enter a number: "))
total=0
while(num>0):
    ld=num%10
    total+=ld
    num=num//10
print("total =",total)    

# write above code by using string method


# sum of squres of given number

num=int(input("Enter a number: "))
total=0
while(num>0):
    ld=num%10
    squ=ld**2
    total+=squ
    num=num//10
print("total =",total)  

# sum of cube of given number

num=int(input("Enter a number: "))
total=0
while(num>0):
    ld=num%10
    squ=ld**3
    total+=squ
    num=num//10
print("total =",total)  


# write code for to count the no of numbers in a given number
num= int(input("Enter a number: "))
count=0

while(num>0):
    ld=num%10
    count+=1
    num=num//10
print("NO.of numbers is =",count)    

# reve a number by using while loop without convert into a string  and check for plgram or not

num=int(input("Enter a number: "))
num1=num
print("num1=",num1)
rev_num=0

while(num>0):
    ld=num%10
    rev_num=rev_num*10+ld
    num=num//10

print("rev_num=",rev_num)   

if(num1 == rev_num):
    print("plgram")
else:
    print("not a plgram")


# amstrong number
# 1^3+2^3+5^3 use cases(153,370,1643,54748)
num= int(input("Enter a number: "))
num1=num
count=0
total=0

while(num>0):
    ld=num%10
    count+=1
    num=num//10
    print("NO.of numbers is =",count) 
    squ=ld**count
    total+=squ
print("num=",num)
print("total=",total) 
if(num1==total):
    print("amstrong number")
else:
    print("not a amstrong number")  
    

def armstrong(num):

 a= num 
 count = 0
 total = 0

 n = num
 while n > 0:
    count += 1
    n = n // 10
 print("count=",count) 

 n = num
 while n > 0:
    ld = n % 10
    total += ld ** count 
    n = n // 10
 print("total=",total)

 if (a == total):
    print(f"{num} is a Armstrong number")
 else:
    print(f"{num} is Not an Armstrong number")

armstrong(123)
armstrong(153)
armstrong(370)
armstrong(1643)
armstrong(54748)


