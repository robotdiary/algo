T = 10
bracket = {
    '(': ')', '[': ']', '{': '}', '<': '>'
}
for tc in range(1, T+1):
    check_len = int(input())
    check = input()
    stack = []
    result = 0
    for i in check:
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        # elif 둘 중에 하나일거니까. if는 낭비겠다
        elif i in [')', ']', '}', '>']:
            if len(stack) and bracket[stack.pop()] == i:
                result = 1
            else:
                result = 0
                break
    if len(stack):
        result = 0
    print(f'#{tc} {result}')