#1
fruits =["apple","mango","banana",]
print(fruits)
#first element and last element
print("first,last element is",fruits[0],fruits[2])
#length of the list
print("length is=",len(fruits))
#replace the second element with "pineapple"
fruits[1] = "pineapple"
#print the modified list
print(fruits)


#2
x=["harish","naresh","suresh","mahesh"]
print(x)
#id of x before change
print("before change id=",id(x))
#change the third element to "kiran"
x[2]="kiran"
#print the modified list
print(x)
#id of x after change
print("after change is is=",id(x))


#3
data =[1,2,[4,5],[6,7],8,["something"]]
print(data)
#print 4,7 from the nested list
print("to print 4=",data[2][0])
print("to print 7=",data[3][1])
#print m from the string "something"
print(data[5][0][2])


#4
mixed =[1,2,"hi",12.5,True]
print(mixed)
#print
print(f"value: {mixed[0]}, type: {type(mixed[0])}")
print(f"value: {mixed[1]}, type: {type(mixed[1])}")
print(f"value: {mixed[2]}, type: {type(mixed[2])}")
print(f"value: {mixed[3]}, type: {type(mixed[3])}")
print(f"value: {mixed[4]}, type: {type(mixed[4])}")




