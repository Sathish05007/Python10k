# 1. Create a tuple of fruits.
fruits = ("apple", "banana", "cherry")
print(fruits)

# 2. Access the first fruit.
print(fruits[0])

# 3. Slice the tuple to get first 2 fruits.
print(fruits[:2])

# 4. Find the length of the tuple.
print(len(fruits))

# 5. Count occurrences of 'apple'.
print(fruits.count("apple"))

# 6. Find the index of 'banana'.
print(fruits.index("banana"))

# 7. Create a tuple with mixed data types.
mixed = (10, "hello", 3.14, True)
print(mixed)

# 8. Unpack tuple elements into variables.
a, b, c = (1, 2, 3)
print(a, b, c)

# 9. Concatenate two tuples.
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)

# 10. Repeat tuple elements.
print(tuple1 * 3)

# 11. Check if 'banana' is in fruits.
print("banana" in fruits)

# 12. Convert list to tuple.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# 13. Tuple inside a tuple (nested tuple).
nested = (1, (2, 3), 4)
print(nested[1][0])

# 14. Maximum value in a numeric tuple.
nums = (5, 10, 15, 2)
print(max(nums))

# 15. Minimum value in a numeric tuple.
print(min(nums))