
n = int(input())

for i in range(n):
    a = list(input())
    b = []
    top = -1
    for j in range(len(a)):
        b.append(a.pop())
        top += 1
        if(len(b) == 1):
            continue
        else:
            if(b[top-1] ==')' and b[top] == '('):
                b.pop()
                b.pop()
                top -= 2

    if len(b) == 0:
        print('YES')
    else:
        print('NO')


# 보통 검색하면 나오는 코드, 정석 풀이법인것 같다. 왜인지 모르지만 처음 배열 마저 스택처럼 풀어버렸다. (거꾸로 생각함)
# 사실 그냥 a를 처음부터 탐색하며 여는 괄호면 스택에 넣고 닫는 괄호인데,
# 스택이 비어있는데 닫는 괄호는 존재할 수 없다.
# 여는 괄호를 +1, 닫는 괄호를 -1로 해서 푸는 방법도 있다 결국에는 짝맞추기라 0이면 답
# t = int(input())
# for _ in range(t):
#     stk = []
#     s = input()
#     isVPS = True
#
#     for ch in s:
#         if ch == '(':
#             stk.append('(')
#         if ch == ')':
#             if stk:
#                 stk.pop()
#             elif not stk:
#                 isVPS = False
#                 break
#     if not stk and isVPS:
#         print('YES')
#     elif stk or not isVPS:
#         print('NO')





