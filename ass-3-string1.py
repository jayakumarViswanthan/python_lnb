string= input("enter a string")
length=len(string)
if length<7:
    print(string[::2])
else:
    print(string[1::2])
