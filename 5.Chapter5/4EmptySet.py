# This will create an empty dictionary not an empty set.
s = {}
print(type(s))

# An empty set can be initialised as :
b = set()  # Set Initialised
print(type(b))

b.add(34)
b.add(3)
b.add(28)
b.add(56)
b.add(3)  # Won't get add, as it is repeatitive
# b.add([21, 32, 62]) # A list can't be added to a set because it is not hashable(An unique identity)
# b.add({21:88}) # A dictionary can't be added to a set because it is not hashable(An unique identity)
b.add((21, 32, 62))  # A tuple can be added to a set
print(b)
