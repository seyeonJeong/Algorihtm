

h,w = map(int,input().split())


a = []
for i in range(h):
    a.append([])
    for j in range(w):
        a[i].append(0)

n = int(input())

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for i in range(l):
            a[x-1][y-1+i] = 1 # x의 값을 그대로 고정 (가로)
    else:
        for i in range(l):
            a[x-1+i][y-1] = 1 # y의 값을 그대로 고정 (세로)

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()


