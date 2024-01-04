cal = {'+': 1, '*': 2}
t = 10
for tc in range(1, t+1):
    n = int(input())
    a = input()
    answer = 0
    eq = ''
    stack = []
    # 후위 표기식으로 변환
    for char in a:
        if char in cal:  # + * 면
            while stack and stack[-1] != '(' and cal[stack[-1]] >= cal[char]:
                eq += stack.pop()
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                eq += stack.pop()
            stack.pop()
        else:
            eq += char
    while stack:
        eq += stack.pop()

    # 계산
    for e_char in eq:
        if e_char in cal:
            if len(stack) < 2:
                answer = 'error'
                break
            a2, a1 = stack.pop(), stack.pop()
            if e_char == '+':
                stack.append(a2 + a1)
            elif e_char == '*':
                stack.append(a2 * a1)

        else:
            stack.append(int(e_char))
    else:
        if len(stack) == 1:
            answer = stack.pop()
        else:
            answer = 'error'

    print(f'#{tc} {answer}')