import sys
from collections import deque

str = deque(input())

n = int(sys.stdin.readline())
top = len(str)-1
for i in range(n):
    ope = input()
    if ope == 'L':
        if top != -1:
            top -= 1
    elif ope == 'D':
        if top != len(str)-1:
            top += 1
    elif ope == 'B':
        if top != -1:
            del str[top]
            top -= 1
    elif ope[0] == 'P':
        top += 1
        str.insert(top,ope[2])

answer = ''.join(s for s in str)
print(answer)



