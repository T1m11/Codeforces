k, n, w = (int(x) for x in input().split())
sum = 0
for i in range(1,w+1):
    sum = sum + k * i
answer = sum - n
if sum <= n:
    answer = 0
print(answer)