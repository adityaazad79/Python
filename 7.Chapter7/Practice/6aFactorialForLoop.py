n = int(input("Enter the number to get factorial of : "))
s = 1
for item in range(1,n+1):
    s *= item
print(s)