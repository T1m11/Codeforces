a = [7,4,90,8,4]

def connect(q,b):
    s = []
    i = j = 0
    while i < len(q) and j < len(b):

        if q[i] < b[j]:
            s.append(q[i])
            i += 1
        else:
            s.append(b[j])
            j += 1
    if i == len(q):
        while j<len(b):
            s.append(b[j])
            j += 1
    if j == len(b):
        while i < len(q):
            s.append(q[i])
            i +=1
    return s

def sor(d):
    if len(d) == 1:
        return d

    mid = len(d)//2
    left = sor(d[:mid])
    right = sor(d[mid:])
    print(left, right)
    return connect(left, right)

print(*sor(a))