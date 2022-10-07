b = [4,6,25,87,3]
def shaker(s):
    f = True
    start = 0
    end = len(s)-1
    while f == True:
        f = False
        for i in range(start,end):
            if s[i]>s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                f = True
            if f == False:
                break
            else:
                f = False
                end = end - 1
                for j in range(end,start-1,-1):
                    if s[i] > s[i+1]:
                        s[i],s[i+1]=s[i+1],s[i]
                        f = True
                        start -= 1
print(shaker(b))