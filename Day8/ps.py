#Problem Solving in Python
#process:-
# identify problem
#design logical code
#implement it

#steps
#understand the problem,make problem into small parts,design solutions for each parts,write code for them,check for errors

#importance :-
#optimizing the code,improve the logical building,it solve real world problems,interviews

#problem solving with for loop & conditional statements

# for loops used for iterate over a sequence
for i in range(0,5):
    print("i=",i)

#condition statements
#it is used to execute sution condations
x=10
if(x>5):
    print("X is big")
else:
    print("x is small")

#print even numbers 1 to 20

for i in range(1,21):
    if(i%2==0):
        # print(f"{i} ") 
        print(i,end=" ")

#print odd numbers 1 to 100
for i in range(1,101):
    if(i%2!=0):
        print(i, end=" ") 

#print numbers divided by 5(1 to 50)
for i in range(1,51):
    if(i%5==0):
        print(i,end=" ")

#print multi of 3,5,3&5
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(f"{i} is both 3,5")
    elif(i%3==0):
        print(i,"multi of 3")
    elif(i%5==0):
        print(i,"multi of 5")
    else:
        print(i,"multi of non")

#print the number of numbers divided by 3,7
x=0
for i in range(1,101):
    if(i%3==0 and i%7==0):
        print(i)
        x +=1
print("number of numbers is=",x)        

#print all upper & lowe case and count them

str1="SaGarEjjAGIri"
print(len(str1))
count1=0
count2=0
for chr in str1:
    if(chr.isupper()):
        print(chr,"upper")
        count1 +=1
    else:
        print(chr,"lower")
        count2 +=1
print("upper=",count1)
print("lower=",count2)

print(len(str1)==(count1 + count2))


#ASSINMENT ON PROBLEM SOLVING
#1.printall the perfect squre from 1 to 100

for i in range(1,101):
   if((i**0.5).is_integer()):
         print(i,"perfect sqr number")
   #else:
         #print(i,"not a perfect squ number")

#2.print all prime numbers 1 to 100
for i in range(1,101):
   if(i>=2 or i==3 or i==5 or i==7): 
      print(i)
   elif(i%2!=0 or i%3!=0 or i%5!=0 or i%7!=0):
      print(i)
   else:
      print("not a prime")

for i in range(2, 501):  # start from 2 because 1 is not prime
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i)
    elif (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        print(i)