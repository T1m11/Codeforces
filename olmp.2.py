X = int(input())
Y = int(input())
N = int(input())
A = X+Y
S = N//A * 2
if N % A == 0:
    print(S)
else:
    if N % A <= Y:
        print(S+1)
    else:
        print(S+2)