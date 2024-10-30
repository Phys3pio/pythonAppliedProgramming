room=int(input())
n=4
if room <=8:
    print(room,1)
else:
    for i in range(1,n+1):
        if room//i<=8:
            print(room//i,i)
            break