s = int(input())
e = int(input())
N = int(input())
ts = 100000000
te = 100000000
x = 100000
for i in range(N):
    x = int(input())
    if abs(s - x) < ts:
        ts = abs(s - x)
    if abs(e - x) < te:
        te = abs(e - x)
print(min(abs(e - s), ts+1+te))
