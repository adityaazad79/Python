# Use open function to read the content of a file
f = open(
    "/home/aditya/Documents/Learning/PythonWithHarry/9. Chapter 9/another2.txt", "a"
)  # Opening the file in append mode
f.write(
    "Aditya is adding this to the file\n"
)  # This will append this line(string) to the file everytime we run this program
f.close()