import sys
from collections import deque

str = list(input())
stack_l = []
#두개의 스택으로 나누는 문제이다. 커서를 따로 구현하지 않고 pop append로 해결해야한다
n = int(sys.stdin.readline())

for i in range(n):
    ope = input()
    if ope == 'L':
        if str:
            stack_l.append(str.pop())
    elif ope == 'D':
        if stack_l:
            str.append(stack_l.pop())
    elif ope == 'B':
        if str:
            str.pop()
    elif ope[0] == 'P':
        str.append(ope[2])

answer = ''.join(s for s in str)
print(answer)



