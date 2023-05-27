import sys

n = int(sys.stdin.readline())
stack = []
sum = 0

for _ in range(n):

    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

for i in stack:
    sum += i

print(sum)
