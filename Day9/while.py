# WHILE LOOP
# this loops runs util the condtion is false


list=[4,10,18,20,55]
x=0
while(x<len(list)):
    print(list[x])
    x+=2

# print even numbers 1 to 20

x=2
total=0
while(x%2==0 and x<=20):
    print("even number =",x)
    x+=2
    total+=x
print(total)


x=1
while(x%2!=0 and x<=20):
    print("odd number =",x)
    x+=2    
   
str="sagar"
# rev_str=" "
for char in range(len(str)-1,-1,-1):
    # print(str)
    print(str[char], end=" ")
  

str="dad"
str_1=""
for char in range(len(str)-1,-1,-1):
    print(str[char])
    str_1 += str[char]
print(str_1)   
if(str==str_1): 
    print("plagram")
else:
    print("not platgram")
