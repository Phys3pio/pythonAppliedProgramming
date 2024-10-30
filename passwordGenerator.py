import random as r
fir="0123456789"
sec="abcdefghijklmnopqrstvwxyz"
thr="ABCDEFGHIJKLMNOPQRSTVWXYZ"
pas=''
g=''
pog=0
n=0
while n==0:
    print("Введите длину пароля")
    n=int(input())
    if n<3:
        print("Пароль должен быть от трех символов")
        n=0
while pog!=1:
    if g.find('1')==-1 or g.find('2')==-1 or g.find('3')==-1 or len(g)==0:
        g=""
        for i in range(1, n + 1):
            f = r.randint(1, 3)
            g = g + str(f)
    else:
        break
for i in range(0,len(g)):
    if g[i]=='1':
        m=r.randint(0, 9)
        pas=pas+fir[m]
    if g[i]=='2':
        m=r.randint(0,24)
        pas=pas+sec[m]
    if g[i]=='3':
        m=r.randint(0, 24)
        pas=pas+thr[m]
    else:
        pas=pas
print("Ваш пароль:",pas)