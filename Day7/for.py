#Loops


for x in range(10): # all Loops start froms zero ends at 9(single argument)
    print("x=",x)



for i in range(2,10): # in this  loop it start from 2 to end at 9
    print("i=",i)    


for i in range(2,10,2): # it means i+=2 ----->2,4,6,8
    print(i)    



for i in range(1,11):
    a=i*2
    print(f" 2 X {i} = {a}")

num=int(input("Enter a number: "))
def mul(num):
    for x in range(1,11):
      print(f"{num} x {x} = {num*x}")
mul(num)      


for i in range(1,11):
    print(f"{i}={i**2}")


for x in range(1,11):
  if(x%2==0):
    print(x**2)
  else:
   print(x**3)

for i in range (1,21):
     if(i%2==0 and i%3==0):
       print(f"{i} fizz-buzz")  
     elif(i%2==0):
       print(f"{i} is fizz")
     elif(i%3==0):
       print(f"{i} buzz")  
     else:
      print(i)   

sum=0
for i in range(1,10):
   sum+=i
   print(sum)
   
sum = 0
for i in range(0, 10):
    sum += i
print(sum)


sum=0
for i in range(1,11):
   sum += i**2
print(sum)    