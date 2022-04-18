# Using recursive

def sum(num):
    if (num == 1):
        return 1
    else:
        return num+sum(num-1)

n = 100
print(sum(n))