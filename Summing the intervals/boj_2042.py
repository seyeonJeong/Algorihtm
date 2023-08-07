n,m,k = map(int,input().split())

list = [0 for _ in range(n)]

for i in range(n):
    list[i] = int(input())



for j in range(m+k):
    a, b, c = map(int, input().split())
    if (a == 1):
        list[b-1] = c
    else:
        print(sum(list[b-1:c]))







