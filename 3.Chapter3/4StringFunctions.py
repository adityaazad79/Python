story = "Once upon a time there was a king whose name was Ashoka. He was a kind person"

#  Striong Functions

# Prints the number of characters of the string

print("length : ", len(story))

# Prints True/False if the string ends with the given value(s)
print("Ends with :", story.endswith("person"))

# Counts the no of occurance(s) of a cheracter(s)
print("Occurance :", story.count("ki"))


# Capitalizes the first letter of the string
story = "once upon a time there was a king whose name was Ashoka. He was a kind person"
print("Capitalize :", story.capitalize())

# Finds the first ocuurence of a character and returns its starting index. If not found, returns -1.
print("Find index :", story.find("king"))

# Reolaces a character(s) with a defined new onw int the whole string
print("Replace :", story.replace("Ashoka", "Shivaji"))
