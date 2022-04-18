# // Write a program to check whether a given number is prime or not using loops.
# // Logic - Prime number has a total no of factor(s) = 2.
# // Using 'while' loop.

b = 1
c = 0
a = int(input("Enter the number to check prime for : "))
if (a < 2):
    print("Prime Number starts from 2\n")
else:
    while (b <= a):
        if (a % b == 0):
            c += 1
        b += 1
    if (c == 2):
        print(a, "is a prime number\n")
    else:
        print(a, "is not a prime number\n")