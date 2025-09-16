#List function 
#1Append()===> IT ADD ONE ELEMENT TO THE END OF THE LIST
my_list=[1,3,4]
print(my_list)
my_list.append(5)
print(my_list)

#2 Extend ==> IT ADD MORE THAN ONE ELEMENT TO THE LIST
my_list.extend([6,7,8,9,10])
print(my_list)

#Insert==> IT ADD AN NEW ELEMENT AT AN A INDEX
my_list.insert(1,2)
print(my_list)

#Remove ==> IT IS USED TO REMOVE IN ELEMENT
my_list.remove(10)
print(my_list)

#Pop()==> IT IS USED TO REMOVE THE LAST ELEMENT IN THE LIST
my_list.pop() # we can also give index value too.pop(3)
print(my_list)

#Count==> IT IS USED TO COUNT THE(REPET ELEMENTS ONLY) ELEMENTS IN A LIST 
my_list2=[1,1,2,3,4,3,5,6,7,3,3,8,9]
print(my_list2.count(3))

#Clear ==> IT MAKE THE LIST EMPTY
my_list2.clear()
print(my_list2)

#Tuples
my_tuple=(1,2,3,4,5,6,7,7)
print(my_tuple)

#count
print(my_tuple.count(7))

#index
print(my_tuple.index(7,7))

#Packing & un-Packing
#Packing==> COMBAINING MULTIPULE VALUES IN TO A SINGLE VALUE

data=1,2,3,4,5,6,7,8,9
print(data)

#un-Packing  ==> ACCESSING THE EACH ELEMENT from the data YOU MUST PASS SAME NUMBER OF VARIBLES THAT IS EQUAL TO THE NUMBER OF VALUES
#IF YOU DON'T KNOW THE NUMBER OF VALUES WE USE (*A) ARBITARY VARIBLES
a,b,c,d=data
print(a)
print(b)
print(c)
print(d)

a,*b,c=data
print(a)
print(b)
print(c)




