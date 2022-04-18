def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "     Aditya is a good boy        "
n = remove_and_strip(this, "Aditya")
print(n)