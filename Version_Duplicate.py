list1=["V2_abc","V33_sh","V45_hdj","V2_jsdh",'V33_hjk']

h=[]
b=[]
list4=[]
for i in list1:
    h=i.split("_")
    b.append(h[0])
print(b)
for i in b:
    b.remove(i)
    if i in b:
        list4.append(i)

for i in list4:
    for j in list1:
        if i in j:
            print(j)
"""c=[]
s=set()
for i in list1:
    prefix,b = i.split('_')
    if prefix in s:
        c.append(i)
    else:
        s.add(prefix)
print(c)"""