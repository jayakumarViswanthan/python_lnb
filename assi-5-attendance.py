
data=['YNY','YYY','NYY','YYY','YYY','YYY','YYN','YYY','YYY']
max1=[]
for i in range(len(data)):
    count=0

    while 'YYY' == data[i]:
        count=count+1
        if i != len(data)-1:
            i=i+1
        else:
            break
    max1.append(count)
print(max(max1))
