for i in range(1,6):
    print(i * "*")   


for i in range(1,6):
    str=""
    for j in range(i):
        str+= "*"
    print(str)  

print(" ")

# # for i in range(1,6):
# #     print(i* f"{i}")    

for i in range(1,6):
    ld=0
    for j in range(i):
        ld=ld*10+i
    print(ld)   

print(" ")

for i in range(1,6):
    ld=0
    for j in range(i+1):
        ld=ld*10+j
    print(ld)  

print(" ")

str="sathish"
new_str=""
for i in range(len(str)):
    new_str+= str[i] 
    print(new_str)    

print(" ")

# str="abcde"
# new_str=""
# count=0
# for i in str:
#     count+=1
#     print(i*count)

print(" ") 

for i in range(97,102):
    ld=""
    for j in range(97,i+1):
        ld += chr(i)
    print(ld)  

print(" ")
str="abcde"
new_str=""
for i in str:
    new_str += i
    print(new_str) 

print(" ")    

for i in range(97,102):
    ld=""
    for j in range(97,i+1):
        ld += chr(j)
    print(ld)  
  
print(" ")

str="something"
new_str=""

for i in str:
    new_str += i #here we can use two loopes too but no need
    print(new_str)    

print(" ")

ld=0
for i in range(1,6):
        sq=i*i
        if(sq <10):
                ld=ld*10+sq
        else:     
               ld = ld* 100 + sq 
               print(ld)  

print(" ")

# print 1
#       44
#       999
#       16161616
#       2525252525




# ----------IN REV ORDER ------------

# *****
# ****
# ***
# **
# *

for x in range(5,0,-1):
    str=""
    for y in range(x):
        str+="*"
    print(str)  

print(" ")
# print above all provlems in rev order and  amstrong num,all peft num,sunny,neyan 

for i in range(6,0,-1):
    ld=0
    for j in range(i):
        ld=ld*10+i
    print(ld)   

print(" ")
for i in range(6,0,-1):
    ld=0
    for j in range(i+1):
        ld=ld*10+j
    print(ld)  

print(" ")
for i in range(102,96,-1):
    ld=""
    for j in range(97,i+1):
        ld += chr(i)
    print(ld)          

print(" ")

# for i in range(6,0,-1,):
#     ld=0
#     for j in range(i):
#         ld=ld*10+i*i
#     print(ld)  


# print(" ")
