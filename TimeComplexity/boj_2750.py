import sys

n = int(sys.stdin.readline())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))


for i in range(n):
    for j in range(i,n):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]


print(list)



