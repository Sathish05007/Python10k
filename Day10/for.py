for i in range(5):
    if (i +1 ==3):
      break
    print("i=",i)
    print("Loop End")

t=[[1,2],3]
print(t[0])
t[0].append(4) #add values at the end of list
print(t)


s=""
for i in range(4):
    if(i%2==0):
        s+="A"
    else:
        s+="B"
print(s)        

word="python3"
print(word[1:4] + word[-1] + word[:1])

my_list=[2,3,5,7]
print(str(my_list[1:4]) + str(my_list[-1]) + str(my_list[:1]))

print((3+4)*2**2-5)

num_list=[1,2,3,4,5,6,7,8,9,10]
count1=0
count2=0
for num in num_list:
    if(num%2==0):
        count1 +=1
    else:
        count2 +=1
print("count1=",count1)
print("count2=",count2)


num_li=[10,43,28,57,23,40,99]
large_num=num_li[0]

for num in num_li:
    if(num>large_num):
        large_num=num
print("large number in list is=",large_num) #without using max()  

str="madam"
palgram=True
for i in range(len(str)//2):
  if(str[i]!=str[-(i+1)]):
    palgram=False
    break
if(palgram):
  print(f"{str} ,is a plgram")
else:
  print(f"{str} ,not a palgram")  


str="sagar"
rev=str[::-1]
if(str==rev):
  print(f"{str}, palgram")
else:
  print(f"{str}. not a plgram")


str="abc12345xyz"
sum=0
for i in str:
    if i in "0123456789":
        sum += int(i)
print(sum)        

list1=[1,2,2,3,1]
list_2=[]
for i in list1:
    if i not in list_2:
        list_2.append(i)
print(list_2)        

for i in range(1,51):
    if i>1:
        for x in range(2,i):
            if i%x==0:
                print(i, "non")

                break
        else:
            print(i,"prime")