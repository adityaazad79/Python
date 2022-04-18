l1 = [1, 8, 7, 2, 21, 15, 7]

# Sorting a list
# l1_sorted=l1.sort() # It doesn't stores sorted l1 list in l1_sorted.
l1.sort()
print(l1)

# Reversing the list
l1.reverse()
print(l1)

# Appending (Adding at the end)
l1.append(45)
print(l1)

# Inserting at an index
l1.insert(0, 32)  # Inser value 32 at index 0
print(l1)

# Deleting index at an index
l1.pop(1)  # Deleting element at index 1. i.e 21
print(l1)

# Deleting/Removing a certain value but only one time
l1.remove(7)
print(l1)
