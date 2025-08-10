# 1. Create a list of 5 numbers and print it.
numbers = [10, 20, 30, 40, 50]
print(numbers)

# 2. Access the 3rd element of the list.
print(numbers[2])

# 3. Slice the list to get first 3 elements.
print(numbers[:3])

# 4. Append a new element to the list.
numbers.append(60)
print(numbers)

# 5. Insert an element at index 2.
numbers.insert(2, 25)
print(numbers)

# 6. Remove an element by value.
numbers.remove(25)
print(numbers)

# 7. Remove element at index 1.
numbers.pop(1)
print(numbers)

# 8. Find the index of 40.
print(numbers.index(40))

# 9. Count how many times 10 appears.
print(numbers.count(10))

# 10. Reverse the list.
numbers.reverse()
print(numbers)

# 11. Sort the list in ascending order.
numbers.sort()
print(numbers)

# 12. Sort the list in descending order.
numbers.sort(reverse=True)
print(numbers)

# 13. Extend the list with another list.
numbers.extend([70, 80, 90])
print(numbers)

# 14. Use list comprehension to create a list of squares from 1 to 5.
squares = [x**2 for x in range(1, 6)]
print(squares)

# 15. Check if 50 is in the list.
print(50 in numbers)