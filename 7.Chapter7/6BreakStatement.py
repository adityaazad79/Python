for i in range(3, 12):  # Prints numbers from 3 to 5
    print(i)
    if i == 5:
        break  # Get out of the loop when i becomes 5
else:  # Else part won't execute as it has been terminated by a break statement
    print("The is for-else")
