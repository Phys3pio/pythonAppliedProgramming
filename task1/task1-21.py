a=[int(x) for x in input().split()]
b=[]
for i in range(1,len(a)):
    b.append(a[i]/(0.01*i))
print(max(b))