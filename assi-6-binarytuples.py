num =int(input("enter integer btw 10 and 20"))
binary=bin(num)
print(binary)
binarytuple=tuple(binary)
print(binarytuple)
print(int(binarytuple[-1]) and int(binarytuple[-2]))
print(int(binarytuple[-1]) or int(binarytuple[-2]))


