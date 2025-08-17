# 1. Check if a Number is a Multiple of 3, 5, or Both*


num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is a multiple of both 3 and 5.")
elif num % 3 == 0:
    print(f"{num} is a multiple of 3.")
elif num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 3 or 5.")




# 2. Function to Check Whether a Number is a Palindrome*


def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse

# Example usage:
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")




#3. Sum of All Even Numbers in a List*


numbers = [10, 15, 22, 33, 40, 55]
even_sum = 0

for i in numbers:
    if i % 2 == 0:
        even_sum += i

print("Sum of even numbers:", even_sum)




#4. Function to Reverse a String (Without Using Built-in Functions)*


def reverse_string(s):
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev


text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))


#STRING METHODES/FUNCTIONS

str="   sAgAr ejJaGirI   "
print("str =",str)

print("")

#len():-IT IS USED TO FIND THE LENGHT OF THE STRING
print("Length =",len(str))

print("")

#Upper():- IT IS USED TO CONVERNT STRING TO UPPER CASE
print("Upper =",str.upper())

print("")

#Lower():- IT IS USED TO CONVERT THE ESTRING TO LOWER CASE
print("Lower =",str.lower())

print("")

stR="*****sagar ejjagiri******"
#STRIP:- IT IS USED TO REMOVE THE EMPTY SPACES FORM BOTH END
print("stR =",stR)
print("strip =",stR.strip("*"))

print("")

#Lstrip():-IT REMOVE EMPTY SPACES FROM LEFT-SIDE OF STRING ONLY
print("stR =",stR)
print("Lstrip =",stR.lstrip("*"))

print("")

#Rstrip():-IT REMOVE EMPTY SPACES FROM RIGHT-SIDE OF STRING ONLY
print("stR =",stR)
print("Rstrip =",stR.rstrip("*"))

print("")

#REPLACE():-IT IS USED REPLACE A WORD OR CHARACTR FROM A STRING
name="I like java and am learning java from 6 months and i want to become a java developer"
print("Name =",name)
print("Replace =",name.replace('java','python'))

#JOIN:-IT COMBINE MORE THAN TWO STRINGS

s1=["I","am","python","developer"]
# print(s1.join(s2,s3,s4))
# print("Join =",join.(s1))

print("")

#DICT
#in dict we use len(),key(),value(),update(),remove(),clear(),
student={
    "name":"sagar",
    "course":"python",
    "city":"Hyd",
    "fav_food":"pappu&sambar"
}
print("dict =",student)

print("")

#len:- print the length of the dict
print("Length =",len(student))

print("")

#Keys:it print only keys
print("keys =",student.keys())

print("")

#Value:- it pirnt only values
print("values =",student.values())

print("")

student_sagar={
    "phone_no":123876543,
    "address":"KNR"
}
print(student_sagar)

print("")

#update:-It update the dict
student.update(student_sagar)
print("Update =",student)

print("")

#clear():-It Will make the dict empty
student.clear()
print("Clear =",student)



#SET:-
# # set2=set() #we create an a empty by using set() methode
# set2={}
# print(type(set2))# if we can't use set() methode it treate as a dict 

set1={2,3,5,7,11,13}
print("Set =",set1)

#add(): add one element to the set
set1.add(19)
print("Add =",set1)

#update: add more than one element to the set
set1.update([4,6],(8,10))
print("Update =",set1)

# #remove(): it remove an element form the set if the element not in the set it display error
# set1.remove(0)
# print("Remove =",set1)

#discars(): it is also remove an element from the set and if the element is not in the set it don't display any error
set1.discard(0)
print(set1)


num = int(input("number: "))
for i in range(1,num+1):
    list1=[]
    for j in range(1,i+1):
        list1+=[j*j]
    print(*list1)    