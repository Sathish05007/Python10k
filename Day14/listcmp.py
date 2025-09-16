list1=[]
for i in range(1,10):
    if(i%2==0):
        print(list1.append(i+2))
print(list1)        

#COMPREHENSION ====> it is a combo of iteration,filteration(optional methode) and expression
#types--> list,tuple,set,dictionary 

data=[i+2 for i in range(1,10)]
print(data)

squre=[i*i for i in range(1,21)]
print(squre)

list=["sai","sagar","sathih","laddu"]
uppe=[i.upper() for i in list]
print(uppe)


# i wana print sq.of numbers fro 10,30 only even
data=[i*i for i in range(10,31) if i%2==0]
print(data)

list1=["hell","hie","hello","welcome","king","queen","something","home"]

# op=[i.upper() for i in list1 if len(i)%2==0]
# print(op)



def vowelcount(ip):
    count=0
    for i in ip:
        if(i in ["a","e","i","o","u"]):
            count +=1
    if(count%2==0):
        return True
    else:
        return False
            

op=[i.upper() for i in list1 if vowelcount(i)]
print(op)


# perfacr number 


def pnumber(num): 
 sum=0
 for i in range(1,num):
    if(num%i==0):
        print(i) 
        sum+=i
 if(num==sum):
    print(f"{num}perfact number")
 else:
    print(f"{num} is not a perfact number")       


out=[i for i in range(1,50) if pnumber(i)]
print(out)

def pnumber(num): 
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if num == total:
        print(f"{num} is a perfect number")
        return True
    else:
        print(f"{num} is not a perfect number")
        return False

out = [i for i in range(1, 50) if pnumber(i)]
print("Perfect numbers under 50:", out)

def pnumber(num): 
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return num == total  # Only return True/False, no printing

# Get only perfect numbers from 1 to 49
out = [i for i in range(1, 50) if pnumber(i)]
print("Perfect numbers under 50:", out)


# 100 to 1000 amstrong numbers
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num


armstrong_numbers = [i for i in range(100, 1001) if is_armstrong(i)]
print("Armstrong numbers from 100 to 1000:", armstrong_numbers)


# tuple in comprenaction checkit once


def armstrong(num):

 a= num 
 count = 0
 total = 0

 n = num
 while n > 0:
    count += 1
    n = n // 10

 n = num
 while n > 0:
    ld = n % 10
    total += ld ** count 
    n = n // 10

 if (a == total):
    return True
 else:
    return False

armstrong_numbers = [i for i in range(100, 1001) if armstrong(i)]
print("Armstrong numbers from 100 to 1000:", armstrong_numbers)


def armstrong(num):
    a = num 
    count = 0
    total = 0

    n = num
    while n > 0:
        count += 1
        n = n // 10

    n = num
    while n > 0:
        ld = n % 10
        total += ld ** count 
        n = n // 10

    if a == total:
        return True
    else:
        return False

armstrong_numbers = [i for i in range(100, 1001) if armstrong(i)]
print("Armstrong numbers from 100 to 1000:", armstrong_numbers)


# 1. Perfect Squares:

# A number is a perfect square if the square root of it is an integer.


perfect_squares = [i for i in range(1, 101) if int(i ** 0.5) ** 2 == i]
print(perfect_squares)

#2. Neon Numbers:

# A number is **neon** if the sum of digits of its square equals the number itself.
# (E.g. 9 → 9² = 81 → 8+1 = 9)


neon_numbers = [i for i in range(1, 100) if sum(int(d) for d in str(i*i)) == i]
print(neon_numbers)

#3. Sunny Numbers:

# A number is **sunny** if the next number is a perfect square.
# (E.g. 3 is sunny because 3+1 = 4, which is a perfect square)


sunny_numbers = [i for i in range(1, 101) if int((i+1) ** 0.5) ** 2 == i + 1]
print(sunny_numbers)

#Reversed Strings (Using List Comprehension):

my_list = ["hi", "hello", "welcome", "morning", "king", "queen"]
reversed_list = [word[::-1] for word in my_list]
print(reversed_list)
