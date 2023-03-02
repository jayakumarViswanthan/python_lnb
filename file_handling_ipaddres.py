import re
#s="djkhf dfsjf kklfj 0.0.0.0 dkljkld flkj 193.34.54.67 djkdf sdjgd ojl 1.2.3.4"
file = open(r"C:\Users\ACER\IdeaProjects\python_test\ip_address","r")
a=file.read()
regex=re.compile("\d+\.\d+\.\d+\.\d+")
Stringlist=regex.findall(a)
print(Stringlist)