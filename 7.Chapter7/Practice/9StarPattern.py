# Printing stars on the edges

n = int(input("Enter the number to print start pattern for : "))
print("*" * n)
for i in range(1, n - 1):
    # print("*", " "*(n-4), "*")
    print("*", end="")
    print(" "*(n-2), end="")
    print("*")
print("*" * n)