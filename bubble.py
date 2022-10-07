a = [3, 4, 1, 8]
fl = False
while fl == False:
    fl = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            fl = False
print(a)