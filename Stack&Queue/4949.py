
while True:
    str = input()
    # 문자열이 온점 하나면 끝낸다.
    if str == '.':
        break

    #chk를 true로 설정한다.
    chk = True
    stack = []

    for i in str:
        if i ==')' or i == ']':
            if stack:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        chk = False
                        break
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        chk = False
                        break
            else:
                chk = False
                break
        elif i == '[' or i == '(':
            stack.append(i)



    if not stack and chk:
        print('yes')
    elif stack or not chk:
        print('no')







