def grt(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3

n1 = 23
n2 = 89
n3 = 56
print(grt(n1, n2, n3))