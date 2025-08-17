# perfact number


# PERFACT SQURE NUMBER
num=int(input("Enter a number: "))
isPerfact=False

for i in range(1,num):
    if(i**2==num):
        isPerfact=True
        break
if(isPerfact):
    print(f"{num} is perfact squre number") 
else:
    print(f"{num} is not a perfact squre number")   


# sunny number 
num=int(input("Enter a number: "))
isSunny=False

for i in range(1,num):
    if(i**2 == i+1):
        isSunny=True
        break
if(isSunny):
    print(f"{num} is a sunny  number")
else:
    print(f"{num} is not a sunny  number")    


# Neyan number
num = int(input("Enter a number: "))
squ_Num = num ** 2
sum = 0

while (squ_Num > 0):
    ld = squ_Num % 10
    sum += ld
    squ_Num = squ_Num // 10

if (num == sum):
    print(f"{num} is a Neon number")
else:
    print(f"{num} is not a Neon number")

#prime number

def squ_num(num):

 isPrime=True
 if(num<=1):
    print("Place give greater than one")
 else:
    for i in range(2,num):
        if(num%i==0):
            isPrime=False
            break
    if(isPrime):
        # print(f"{num} is a prime number")
        return True
    else:
        # print(f"{num} is not a prime number")    
        return False


op=[x for x in range(2,51) if squ_num(x)]
op1=tuple(x for x in range(2,51) if squ_num(x) )
op2={x for x in range(2,51) if squ_num(x)}
op3={"prime":x for x in range(2,51) if squ_num(x)}
print(op)
print(op1)
print(op2)
print(op3)

#Fibinanic series

num=int(input("Enter a number: "))
a=0
b=1
count=0
while(count<num):
    print(a,end=" ")
    temp =a+b
    a=b
    b=temp
    count +=1
    # print(count)        