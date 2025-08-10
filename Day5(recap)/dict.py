# 1. Create a dictionary of student details.
student = {"name": "John", "age": 20, "marks": 85}
print(student)

# 2. Access a value by key.
print(student["name"])

# 3. Get value using get() method.
print(student.get("marks"))

# 4. Change a value.
student["age"] = 21
print(student)

# 5. Add a new key-value pair.
student["grade"] = "A"
print(student)

# 6. Remove a key using pop().
student.pop("marks")
print(student)

# 7. Remove last inserted item using popitem().
student.popitem()
print(student)

# 8. Get all keys.
print(student.keys())

# 9. Get all values.
print(student.values())

# 10. Get all items.
print(student.items())

# 11. Update dictionary with another dictionary.
student.update({"city": "New York", "age": 22})
print(student)

# 12. Check if a key exists.
print("name" in student)

# 13. Dictionary comprehension to create squares.
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 14. Nested dictionary example.
school = {
    "student1": {"name": "Alice", "age": 14},
    "student2": {"name": "Bob", "age": 15}
}
print(school["student1"]["name"])

# 15. Clear the dictionary.
student.clear()
print(student)
