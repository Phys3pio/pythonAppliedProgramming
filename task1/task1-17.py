pol = input()
ches=['k','a','b','c','d','e','f','g','h']
for i in range(1,len(ches)+1):
    if (pol[0]==ches[i] and i%2==0 and int(pol[1])%2==0) or (pol[0]==ches[i] and i%2!=0 and int(pol[1])%2!=0):
        print("black")
        break
    elif (pol[0]==ches[i] and i%2!=0 and int(pol[1])%2==0) or (pol[0]==ches[i] and i%2==0 and int(pol[1])%2!=0):
        print("white")
        break