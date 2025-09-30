try:
    x=int(input("Enter X: "))
    y=int(input("Enter y: "))
    print("sum=",x/y)
except ZeroDivisionError:
    print("Enter non zero number")
except ValueError:
    print("Enter numbers only")        

except ValueError as error:
    print("Enter non zero number",error)
except SyntaxError as error:
    print("Enter numbers only",error)     


# List of Common Python Errors

# SyntaxError → Invalid syntax in the code.

# IndentationError → Wrong indentation (spaces/tabs issue).

# NameError → Using a variable that is not defined.

# TypeError → Operation between incompatible data types.

# ValueError → Invalid value passed to a function.

# ZeroDivisionError → Division by zero.

# IndexError → Index out of range in a list/tuple.

# KeyError → Accessing a non-existent key in a dictionary.

# AttributeError → Object has no such attribute or method.

# ImportError → Error when importing a module.

# ModuleNotFoundError → The imported module does not exist.

# FileNotFoundError → File not found when trying to open it.

# IOError → Input/output error when handling files.

# RuntimeError → General runtime error.

# OverflowError → Number too large to represent.

# MemoryError → Out of memory during execution.

# StopIteration → Iterator runs out of items.

# UnboundLocalError → Local variable used before assignment.

# RecursionError → Maximum recursion depth exceeded.

# AssertionError → assert statement fails.



# 1. SyntaxError (can't catch directly, so we simulate)
try:
    eval("print('Hello'")   # Missing parenthesis
except SyntaxError:
    print("Caught a SyntaxError: invalid syntax")

# 2. IndentationError (simulate with eval)
try:
    code = "def f():\nprint('hi')"   # bad indentation
    exec(code)
except IndentationError:
    print("Caught an IndentationError: wrong indentation")

# 3. NameError
try:
    print(x)   # x is not defined
except NameError:
    print("Caught a NameError: variable not defined")

# 4. TypeError
try:
    print("Age: " + 25)
except TypeError:
    print("Caught a TypeError: incompatible types")

# 5. ValueError
try:
    int("hello")
except ValueError:
    print("Caught a ValueError: invalid value for int()")

# 6. ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: division by zero")

# 7. IndexError
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Caught an IndexError: index out of range")

# 8. KeyError
try:
    data = {"name": "Alice"}
    print(data["age"])
except KeyError:
    print("Caught a KeyError: key not found in dictionary")

# 9. AttributeError
try:
    x = 10
    x.append(5)   # int has no append()
except AttributeError:
    print("Caught an AttributeError: object has no such attribute")

# 10. ImportError
try:
    from math import cube   # cube doesn't exist
except ImportError:
    print("Caught an ImportError: cannot import name")

# 11. ModuleNotFoundError
# try:
#     import not_a_module
# except ModuleNotFoundError:
#     print("Caught a ModuleNotFoundError: module does not exist")

# 12. FileNotFoundError
try:
    open("nofile.txt")
except FileNotFoundError:
    print("Caught a FileNotFoundError: file not found")

# 13. IOError (alias of OSError in modern Python)
try:
    f = open("/root/secret.txt")
except IOError:
    print("Caught an IOError: input/output error")

# 14. RuntimeError
try:
    import sys
    sys.setrecursionlimit(5)
    def recurse(): recurse()
    recurse()
except RuntimeError:
    print("Caught a RuntimeError: recursion depth exceeded")

# 15. OverflowError
try:
    import math
    print(math.exp(1000))   # too large
except OverflowError:
    print("Caught an OverflowError: number too large")

# 16. MemoryError
try:
    big = [1] * (10**10)   # huge list
except MemoryError:
    print("Caught a MemoryError: out of memory")

# 17. StopIteration
try:
    it = iter([1, 2])
    print(next(it))
    print(next(it))
    print(next(it))  # no more items
except StopIteration:
    print("Caught a StopIteration: no more items in iterator")

# 18. UnboundLocalError
try:
    def test():
        print(x)
        x = 5
    test()
except UnboundLocalError:
    print("Caught an UnboundLocalError: local variable used before assignment")

# 19. RecursionError
try:
    def loop():
        return loop()
    loop()
except RecursionError:
    print("Caught a RecursionError: maximum recursion depth exceeded")

# 20. AssertionError
try:
    x = 5
    assert x > 10
except AssertionError:
    print("Caught an AssertionError: assertion failed")
