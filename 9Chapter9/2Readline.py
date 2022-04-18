# Use open function to read the content of a file
f = open("/home/aditya/Documents/Learning/PythonWithHarry/9. Chapter 9/sample.txt", "r")

# Read first line
data = f.readline() # Readline will print only the first line of the file if used first time
print(data)

# Read 2nd line
data = f.readline() # Will print 2nd line as it has been used for 2nd time
print(data)
f.close()