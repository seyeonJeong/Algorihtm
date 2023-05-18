
a,m,d,n = map(int, input().split())

for i in range(0,n-1):
    if n == 1:
        break
    a = (a*m) + d

print(a)