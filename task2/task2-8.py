import numpy as np
r=2.5
v=1
vecs = np.array(
 [
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]
 ]
)
for i in vecs:
    print(i)
def closest(v,r,vecs):
    kol = 0
    for i in vecs:
        ev=0
        for j in i:
            ev+=j**2
        if ev**(1/2)<v+r:
            kol+=1
    return kol
print(closest(v,r,vecs))
