Dict = {}
f1 = input("Enter name of the 1st friend\n")
l1 = input("Enter favourite language of the 1st friend\n")
f2 = input("Enter name of the 2nd friend\n")
l2 = input("Enter favourite language of the 2nd friend\n")
f3 = input("Enter name of the 3rd friend\n")
l3 = input("Enter favourite language of the 3rd friend\n")
f4 = input("Enter name of the 4th friend\n")
l4 = input("Enter favourite language of the 4th friend\n")
Dict.update({f1: l1})
Dict.update({f2: l2})
Dict.update({f3: l3})
Dict.update({f4: l4})
print(Dict)

# If the name of two friends are same, the latter's favourite language will replace the former's favourite language