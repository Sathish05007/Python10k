# STRING METHODS
print("=== STRING METHODS ===")
s = "  hello world  "

print("Original String:", repr(s))
print("upper():", s.upper())
print("lower():", s.lower())
print("title():", s.title())
print("strip():", s.strip())
print("replace():", s.replace("hello", "hi"))
print("split():", s.strip().split())  # removes spaces then splits
print("join():", "-".join(["a", "b", "c"]))
print("startswith('  he'):", s.startswith("  he"))
print("endswith('ld  '):", s.endswith("ld  "))
print("find('world'):", s.find("world"))
print("count('l'):", s.count("l"))

# LIST METHODS
nums = [1, 2, 3]
print("Original List:", nums)

nums.append(4)
print("append(4):", nums)

nums.extend([5, 6])
print("extend([5, 6]):", nums)

nums.insert(1, 1.5)
print("insert(1, 1.5):", nums)

nums.remove(1.5)
print("remove(1.5):", nums)

popped = nums.pop()  # removes last
print("pop():", popped, "| List now:", nums)

nums.clear()
print("clear():", nums)

nums = [1, 2, 2, 3, 4]
print("\nNew List:", nums)
print("index(3):", nums.index(3))
print("count(2):", nums.count(2))

nums.sort(reverse=False)
print("sort():", nums)

nums.reverse()
print("reverse():", nums)

copy_list = nums.copy()
print("copy():", copy_list)