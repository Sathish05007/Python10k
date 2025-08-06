#DATA TYPES IN PYTHON
#IT CHACKES THE WHICH TYPE OF DATA A VARIBLES IS HOLDEING IS KNOWN AS DATATYPES
#THEIR ARE TWO TYPES 1)PRIMATIVE 2)NON-PRIMATIVE

#1)PRIMAATIVE :-IT CAN STORE ONLY ONE VALUE AT A TIME && IMMUTABLE IT MEANS THE VALUES CAN'T CHANGE
#EX:-int,float,string,boolen

#2)NON-PRIMATIVE :-IT CAN STORE MULTIPLUE VALUES AT A TIME && MUTTABLE IT MEANS THE VALUES CAN CHANGE 
#EX:-list,set,tuple,Dictionary,
#here tuple is the only non-primative data type which is immutable

#primative data types

a = 10 #int 
print(type(a)) #<class 'int'>
print("a=",a)
print(id(a)) #id is used to check the memory location of the variable

a=15
print(id(a),"a",a) #it will show the new memory location of the variable


b = 10.5 #float
print(type(b)) #<class 'float'>
print("b=",b)
print(id(b)) #id is used to check the memory location of the variable

b=20.5
print(id(b),"b=",b) #it will show the new memory location of the variable

c = "hello" #string
print(type(c)) #<class 'str'>
print("c=",c)
print(id(c)) #id is used to check the memory location of the variable
c="world"
print(id(c),"c",c) #it will show the new memory location of the variable

print("c=",c)
d = True #boolen
print(type(d)) #<class 'bool'>
print("d=",d)




# NON-PRIMATIVE DATATYPES

# List
# A list is a mutable data type that can hold multiple values.
# It is defined using square brackets [] and can contain elements of different data types.
# Lists are mutable, meaning you can change their content without changing their identity.

my_list = ["apple", "banana", "cherry","mango","grapps"]
print("List:", my_list)

print("Type of my_list:", type(my_list))  # <class 'list'>
print("ID of my_list:", id(my_list))  # Memory location of the list
print("Length od List",len(my_list))

my_list[0] = "orange"  # Changing the first element
my_list[len(my_list)-1] = "guva" # Changing the last element
print("Updated List:", my_list)
print("Updated ID of my_list:", id(my_list))  # ID remains the same since lists are mutable 