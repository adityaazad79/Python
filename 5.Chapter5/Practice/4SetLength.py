s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

# Length of the string "s" after operations is 2.

# s = set()
# s.add(20)
# s.add("20.0")
# s.add("20")
# print(s)
# print(len(s))

# But here 20.0 will be considered as a string. i.e unique. So the value set length will be 3
