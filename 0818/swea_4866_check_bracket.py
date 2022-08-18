T = int(input())
bracket = {
    '(': ')', '{': '}'
}
for tc in range(1, T+1):
    check = input()
    stack = []
    result = 0
    for i in check:
        if i in ['(', '{']:
            stack.append(i)
        elif i in [')', '}']:
# 스택이 비어있을 때를 고려해야 한다. ex) 닫는 괄호가 더 많을 때
            if len(stack) and bracket[stack.pop()] == i:
                result = 1
            else:
                result = 0
                break
    if len(stack) != 0: # stack != 0 이라고 하면 안 되네
        result = 0
    print(f'#{tc} {result}')