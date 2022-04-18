# Use open function to read the content of a file
f = open(
    "/home/aditya/Documents/Learning/PythonWithHarry/9. Chapter 9/another.txt", "w"
)
f.write(
    "Aditya is adding this to the file"
)  # Writes this to the file. The previous data will be erased
f.close()