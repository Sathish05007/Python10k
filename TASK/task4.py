i = 1
while i <= 10:
    print(i)
    i += 1


n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        print("First number divisible by 3 and 7:", i)
        break
    i += 1

i = 1
while i <= 10:
    if i == 5 or i == 7:
        i += 1
        continue
    print(i)
    i += 1

# Program to check palindrome using while loop
text = input("Enter a string: ")

start = 0
end = len(text) - 1
is_palindrome = True

while (start < end):
    if text[start] != text[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if (is_palindrome):
    print("Palindrome")
else:
    print("Not a palindrome")

# Program to reverse a number using while loop (no string conversion)
num = int(input("Enter a number: "))
rev = 0

original = num  # Store original number for display

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
