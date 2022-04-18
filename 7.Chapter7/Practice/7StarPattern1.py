n = int(input("Enter the number to print start pattern for : "))
# for i in range(1, n + 1):
#     print(" "*(n-i), "*" * ((2*i)-(1)), " "*(n-i))

for i in range(n): 
    print(" " * (n-i-1), end="") # 'end=""' is used to pent next print statement in the same line
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))