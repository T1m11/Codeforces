N = int(input())
s = []
j = 0
f = False
for i in range(N):
    x = int(input())
    s.append(x)
while f == False:
    f = True
    for i in range(0,N-1):
        if s[i] > s[i+1]:
            s[i], s[i+1] = s[i+1], s[i]
            j += 1
            f = False

print(*s)
print('вот '+ str(j))