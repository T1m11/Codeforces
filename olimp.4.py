N = int(input())
D = int(input())
x = 1
i = 1
while i <= N and i <= x:
    j = int(input())
    x = max(i + j//D, x)
    i += 1
print(min(x, N))
    
