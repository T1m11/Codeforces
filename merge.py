a = [5,3,78,5,9]

def part(a):
    a1 = []
    a2 = []
    m = len(a)//2
    for i in range(m):
        a1.append(a[i])
    for i in range(m,len(a)):
        a2.append(a[i])