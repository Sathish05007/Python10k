for i in range(0,11):
    print("i=",i)

for i in range(0,21,2):
    print("i=",i)


for i in range(10,30):  # for i in range(10,30,2):
    if(i%2!=0):         #     print("i=",i)
      print("i=",i)

for i in range(0,11):
    print(f"{i}=",i**2)

for i in range(1,10):
    print((i))

for i in range(0,51):
    if(i%5==0):
        print("i=",i)

for i in range(0,11):
    print(f"{i}=",i**3)

a=int(input("Enter a number: "))
def table_of_number(a):
 for i in range(1,11):
    print(f"{a} x {i} = {i*a}")
table_of_number(a)    

for i in range(1,11):
    print(i)

for i in range(1,10):
    print(f"{i}=",i**2)    

for i in range(1,10):
    print(f"{i}=",i**3)


a=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{a} x {i}=",a*i)

sum=1
for i in range(1,6):
    sum *= i
print(sum)    