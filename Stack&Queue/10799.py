import sys

bar = list(sys.stdin.readline())
stack = []
result = 0
for i in bar:
    if bar[i] == '(': # 만약 (이면 그냥 스택에 추가한다.
        stack.append('(')
    else: # 만약 ) 이면 두가지 경우로 나뉜다.
        if bar[i-1] == '(': # 이전 값이 ( 인 경우 , pop을 하고, 스택에 있는 값만큼 추가한다.
            stack.pop()
            result += len(stack)
        else: # 이전 값이 ) 인 경우, 막대기의 끝이라는 뜻으로 +1을 해준다.
            stack.pop()
            result += 1
