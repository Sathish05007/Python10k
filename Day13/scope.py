# #three types global,local,enclosed(block level)
# #scope as a access of a varible and life of a varible

x=10
y=20

def add():
    print("add function=",x+y)
add()    

#local and global 
def sum():
    a=20
    b=700
    print("sum function=",a+b-y)
sum()    

def mult():
    p=2
    q=9
    print("multi function=",p*x-q)
    # print(p+q+a) we cant acces the varible a because of it is a local scope varible
mult()     


#enclosed function
def add_1(m,n):

    # print(s+t)
    print("add_1 function=",m+n*x)

    def add_2():
        s=20
        t=5
        print("add_2 function=",s+t)
    add_2()    

add_1(5,10)    


#scope modifiers local to global, enclosed to local 
#use key words like,
# local-->global scope use global key word
# enclosed-->local use nonlocal key word



def fun1():
    global x #we changed the local scope to global scope 
    x=10
    print(x)

fun1()
print(x)


