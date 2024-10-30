melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
b=[]
for el in melt:
    for j in el:
        if j=="O":
            b.append(melt[el])
print(*b)