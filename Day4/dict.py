
# 3. DICTIONARY METHODS
d = {"a": 1, "b": 2}
print("get('a'):", d.get("a"))
print("keys():", list(d.keys()))
print("values():", list(d.values()))
print("items():", list(d.items()))

popped_value = d.pop("a")
print("pop('a'):", popped_value, "remaining:", d)

popped_item = d.popitem()
print("popitem():", popped_item, "remaining:", d)

d.update({"c": 3})
print("update:", d)

d.clear()
print("clear:", d)