# 1. SET METHODS
s = {1, 2}
s.add(3)
print("add:", s)

s.remove(2)
print("remove:", s)

s.discard(5)  # no error if element not found
print("discard:", s)

popped = s.pop()
print("pop (removed element):", popped, "remaining:", s)

s.clear()
print("clear:", s)

set1 = {1, 2}
set2 = {3, 4}
print("union:", set1.union(set2))

set3 = {1, 2, 3}
set4 = {2, 3, 4}
print("intersection:", set3.intersection(set4))
print("difference:", set3.difference(set4))

set1.update([5, 6])
print("update:", set1)


# 2. TUPLE METHODS
t = (1, 2, 2, 3)
print("count(2):", t.count(2))
print("index(3):", t.index(3))
