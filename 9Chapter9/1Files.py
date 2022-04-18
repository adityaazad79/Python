# Use open function to read the content of a file
# f = open("/home/aditya/Documents/Learning/PythonWithHarry/9. Chapter 9/sample.txt", "r")
f = open(
    "/home/aditya/Documents/Learning/PythonWithHarry/9. Chapter 9/sample.txt"
)  # By default, the mode is r(read)
# data = f.read()
data = f.read(8) # This will read only the first 8 characters(including spaces) from the file
print(data)
f.close()
