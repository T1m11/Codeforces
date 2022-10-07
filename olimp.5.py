import math

x = int(input())
y = int(input())
k = 1

if x == y:
    if x == 1:
        print(1)
    else:
        print(-1)
else:
    if x != 1:
        k = math.ceil((x-1)/(y-x))
        print(k*x)
    else:
        print(1)