MyDict = {
    "Key": "Value",
    "Aditya": "A Businessman",
    "Shubham": "Friend",
    "PG": "Paying Guesthouse",
    "Marks": [1, 2, 3],
    "AnotherDict": {"Azad": "India"},  # Dictionary inside a dictionary
    1: 7
}
# Dictionary Methods
print(type(MyDict.keys()))  # Data Type = Dict Keys
print(MyDict.keys())  # Prints all the Keys of the dictionary
print(type(MyDict.values()))  # Data Type = Dict Values
print(MyDict.values(), "\n")  # Prints all the values of the dictionary

# Prints all the (Key,Value) and the dictionry inside the dictionary in tuple form
print(MyDict.items(), "\n")

# Dictionary Update
UpdateDict = {
    "Water": "Life"
}
# Updates the dictionary by adding (Key,Value) from the UpdateDict
MyDict.update(UpdateDict)
print(MyDict)

# Prints a value associated with a key
print(MyDict.get("Shubham"))

# The differcence between .get and [] syntax
# Prints "None" if the key is not present in the dictionary
print(MyDict.get("Sonu"))
print(MyDict["Sonu"])  # Throws error if the key is not found in the dictionary

# More at
# https://docs.python.org/3/tutorial/datastructures.html