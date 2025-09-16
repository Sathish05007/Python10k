#print()
#type()
#id()

#TYPE converction:-
#int-->float===> we use float()
a=20
print(float(a))

#str()-->int===> we use int()
str="55"
print(int(str))

#float()-->int==> we use int()
price=55.78
print(int(price))

#complex()
a=30
img=4
print(complex(a,img))

#max():-

# Purpose:- Returns the largest item from an iterable (like a list, tuple) or among two or more arguments.
# Example
#    max(3, 8, 1) returns 8
#    max([4, 10, 7])  returns 10


# ### 2. min()

#  Purpose: Returns the smallest item from an iterable or among two or more arguments.
#  Example:
#   min(3, 8, 1) returns 1
#   min([4, 10, 7]) returns 4


# 3. sum()

#  Purpose: Adds all the items in an iterable (like a list or tuple) and returns the total.
#  Optional second argument: A value to start the sum from.
#  Example:
#   sum([1, 2, 3]) returns 6
#   sum([1, 2, 3], 10) returns 16 (starts at 10)


# 4. pow()

#  Purpose: Returns the value of x raised to the power y.
#   Optionally, you can pass a third argument: pow(x, y, z) which gives (xy) % z
#   Example:
#   pow(2, 3) returns 8 (2³ = 8)
#   pow(2, 3, 5) returns 3 (8 % 5 = 3)


# 5. round()

#  Purpose: Rounds a number to the nearest integer or to a given number of decimal places.
#  Syntax: round(number, ndigits)

#    ndigits is optional. If provided, rounds to that many decimal places.
#    Example:
#   round(3.14159) returns 3
#   round(3.14159, 2) returns 3.14


# 6. divmod()

#  Purpose: Returns a tuple containing the quotient and the remainder when dividing two numbers.
#  Syntax: divmod(a, b) is equivalent to (a // b, a % b)
#  Example:
#   divmod(10, 3) returns (3, 1)
#   Because 10 // 3 is 3 and 10 % 3 is 1

