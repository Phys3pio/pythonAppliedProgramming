a=[int(x) for x in input().split()]
def my_filter(a):
    for i in range(len(a)):
        a[i]*=10
    return a
print(my_filter(a))