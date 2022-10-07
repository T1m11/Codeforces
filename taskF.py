N = int(input())
a = [ ]
f = False
for i in range(N):
    x = int(input())
    a.append(x)
while f == False:
    f = True
    for i in range(N - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            f = False
print(*a)