for i in range(3, 12):  # Prints numbers from 3 to 11 except 5
    if i == 5:
        continue  # Re-iterate the loop when i becomes 5. i.e 5 won't get printed
    print(i)
else:  # Else part will get executed
    print("The is for-else")