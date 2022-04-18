MyDict = {
    "Key": "Value",
    "Aditya": "A Businessman",
    "Subham": "Friend",
    "PG": "Paying Guesthouse",
    "Marks": [1, 2, 3],
    "AnotherDict": {"Azad": "India"}  # Dictionary inside a dictionary
}
# ccessing Dictionary value by using it's Key value
print(MyDict["PG"])
print(MyDict["Key"])
print(MyDict["Marks"])
# Accessing dictionary inside a dictionary and can't have duplicate keys
print(MyDict["AnotherDict"]["Azad"])
# A dictionary mutable
MyDict["Marks"] = [4, 5, 6]
print(MyDict["Marks"])
