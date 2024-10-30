mass=[float(x) for x in input().split()]
m=max(mass[:10])
for i in range(len(mass)):
    if mass[i]==m:
        print(i)
        break