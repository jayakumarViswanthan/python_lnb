list1=[]
for i in range(1,21):
    list1.append(i)

list2=list1[:5]+list1[-5:]

sqrlist=[x**2 for x in list2 ]
print(sqrlist)
a=sqrlist[:2]
b=sqrlist[2:5]
c=sqrlist[5:]
print(a,b,c)