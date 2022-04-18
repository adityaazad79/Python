n = int(input("Enter the number to print multiplication table for : "))
for i in range (10,0,-1):
    print(n, "X", i, "=", n*i)
    # or
    # print(f"{n} X {i} = {n*i}")