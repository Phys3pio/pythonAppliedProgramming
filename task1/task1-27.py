def volume(a):
    if len(a)==2:
        return a[0]*a[1]
    else:
        return a[0]*a[1]*a[2]
print(volume(input()))