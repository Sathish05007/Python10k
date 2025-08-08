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

# #tuple is a immutable data type it means it cant change the values
# #it is denoted by ()

# days =("sun","mon","tue")
# print(days)
# print(type(days))

# num=(1,2,3,4,5)
# print(num)

tuple_last=("a","b","c","d")
print(tuple_last[-1]) # or print index[4]
print(f"Length of tuple is={len(tuple_last)}")

#set a un-order of collection elementes but it cant allow same values ex:-phone numbers
#set is denoted by{}
#sets are two types noramal sets & frozensets
#it dont have indexing
#in this type of sets we can do add,remove
#add(),remove()
sets={1,2,3,5,7,2,4,2,4,4,}
print(sets)
print(type(sets))
# print(sets[0])

# #frozensets inthis the elements are fix & locked we cant add ,remove
sets1=frozenset([1,2,3,4,6,7])
print(sets1)
print(type(sets1))


set_1={"a","b","c","x","y"}
print(set_1)




student={
    "name": "sagar",
    "age": 25,
    "rollno": 180711,
    "pno": 8977239316,
    "address":{
        "door_no": 1-20,
        "strest_name": "sr nagar",
        "state": "A.P",
        "pincode":505183,
    },
    "is_married": False,
    "skills":["html","css","javascript","reactjs"]
}
print(student)
print(type(student))
print(student["name"])
print(student["pno"])#accessing value by key
print(student["address"]["state"])
print(student["skills"][1])#accessing the elements by the index
#update the values in the dict
student["age"]=19
print(student)
#add more elements

student["fav_food"] =["chiken","allu curry","egg"]
print(student)

#remove the elements
del student["is_married"]   #deleting the key value pair
print(student)

info={
    "names":"sagar",
    "age":25
}
print(info)
print(info["age"])
info["age"] =30
print(info)
info["pno"]=8977239316
print(info)
del info["age"]
print(info)

#nessted dictionary

person_info={
    "aadher_no": 2022199400299,
    "name": "ejjagiri sathish",
    "addres":{
        "h_no": 1-82,
        "villege_Name":"sr nagar",
        "pincode":505183,
    },
    "father_name":"rajaiah"
}
print(person_info)