#TYPE(),ID()
#USER INPUT()


x=5
y=5
z=5
print(id(x)) # the memory range is -5 to 256 same id's it is called as MEMORY POLLING it mainy used for save memory
print(id(y))
print(id(z))

#interning
x="helloxcvbnmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
y="helloxcvbnmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(id(x))
print(id(y))
# this two are called as optimization 

a=5
b=a
print(b)
a=10

