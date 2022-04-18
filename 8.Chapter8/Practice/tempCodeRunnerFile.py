def remove_and_strip(string,word):
    ns=string.replece(word,"")
    return ns.strip()

this="     Aditya is a good boy       "
n=remove_and_strip(this,"Aditya")
print(n)