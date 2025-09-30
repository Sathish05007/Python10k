# 1. Syntax Error Check

# if True
#     print("Hello") 

# 2. ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 3. ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid number for age.")

# 4. TypeError
try:
    x = 10 + "20"   # Invalid operation
except TypeError:
    print("Error: Cannot add integer and string together.")

# 5. Finally Block
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except Exception as e:
    print("Error:", e)
finally:
    print("Program Completed")

# 6. Multiple Exceptions
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

# 7. File Handling Error
try:
    with open("student_data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File 'student_data.txt' not found.")

# 8. Catch All Exceptions
try:
    n = int(input("Enter a number: "))
    print("Square is:", n**2)
except Exception as e:
    print("An unexpected error occurred:", e)

# 9. Custom Error Message
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is:", age)
except ValueError as ve:
    print("Error:", ve)

# 10. Safe Calculator
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            print("Result:", num1 / num2)
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Invalid input, please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

calculator()
