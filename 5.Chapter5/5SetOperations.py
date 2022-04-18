s = {1, 3, 4, 2, 8, 6, 1, 5}
print(len(s))
# Removes the value(all) 1 from the set if the value is not present, throws erroe
s.remove(1)
print(s)

s.pop()  # Removes a value arbitrarily and returns the removed element
print(s)

# Returns the union of both of the sets but doesn't writes on the set
print(s.union({56, 67}))

# Returns the intersection of both of the sets but doesn't writes on the set
print(s.intersection({5, 67}))

s.clear()  # Empties the set
print(s)