# 1. Create a set of numbers.
nums = {1, 2, 3, 4, 5}
print(nums)

# 2. Add an element to the set.
nums.add(6)
print(nums)

# 3. Remove an element using remove().
nums.remove(2)
print(nums)

# 4. Remove an element using discard() (no error if missing).
nums.discard(10)
print(nums)

# 5. Pop a random element.
nums.pop()
print(nums)

# 6. Clear the set.
nums.clear()
print(nums)

# 7. Create two sets and find union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# 8. Find intersection of two sets.
print(set1.intersection(set2))

# 9. Find difference of two sets.
print(set1.difference(set2))

# 10. Find symmetric difference.
print(set1.symmetric_difference(set2))

# 11. Check subset.
print({1, 2}.issubset(set1))

# 12. Check superset.
print(set1.issuperset({1}))

# 13. Convert list to set.
list_nums = [1, 2, 2, 3]
set_nums = set(list_nums)
print(set_nums)

# 14. Frozen set example (immutable set).
frozen = frozenset([1, 2, 3])
print(frozen)

# 15. Set comprehension for squares.
squares = {x**2 for x in range(1, 6)}
print(squares)



