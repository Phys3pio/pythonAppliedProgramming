melt= {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455,'Si': 1415, 'Be': 1287}
el1,el2=str(input()).split()
print(abs(melt[el1]-melt[el2]))