# factorial using recursive method
def fac_rec(num):
    if (num == 1 or num == 0): # Base Condition
        return 1
    return num * fac_rec(num-1) # Function calling itself


n = int(input("Enter the number to find the factorial of : "))
print(fac_rec(n))