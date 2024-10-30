x,y = map(float, input().split())
s1=""
s2=""
if (x-1)**2+y**2==2**2 and (x-1)**2 + y**2==1:
    s1="yes"
else:
    s1="no"
if abs(x-4)<2 and abs(y-2)<3:
    s2="yes"
else:
    s2="no"
print(s1,s2)