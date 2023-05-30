import sys

n = int(sys.stdin.readline())
flag = 0
cur = 0
stack = []
answer = []
for i in range(n):
    num = int(sys.stdin.readline())

    while cur <= num:
        stack.append(num)
        answer.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
























