f = int(input("Enter the full marks for ech subject : "))
s1 = int(input("Enter the marks in subject 1 : "))
s2 = int(input("Enter the marks in subject 2 : "))
s3 = int(input("Enter the marks in subject 3 : "))
p1 = 100*s1/f
p2 = 100*s2/f
p3 = 100*s3/f
p = (p1+p2+p3)/3
if (p1 >= 33 and p2 >= 33 and p3 >= 33 and p >= 40):
    print("Pass")
else:
    print("Fail")