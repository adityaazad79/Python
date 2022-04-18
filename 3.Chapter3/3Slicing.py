name = "Aditya"
# Index
# 0 = A
# 1 = d
# 2 = i
# 3 = t
# 4 = y
# 5 = a
# prints index value(character)
print(name[0])
# name[3] = "d" # Can't be chanaged
print(name[1:3])  # The first value is incluing but second is not included
print(name[:4])  # Same as print(name[0:4])
print(name[0:])  # Same as print(name[0:6])
print(name[:])  # Same as print(name[0:6])
name = "AdityaIsAGoodBoy"
# String slicing with a skip value. Here it's skipping every 2nd value
print(name[::2])

print(name[::-1])  # String Reversal