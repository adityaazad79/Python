n = int(input("Enter the number to print multiplication table for : "))
for item in range(1, 11):
    print(n, "X", item, "=", n*item)
    # or
    # print(f"{n} X {item} = {n*item}")
