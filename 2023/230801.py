cal = {'+': 1, '*': 2}
t = int(input())
for tc in range(1, t + 1):
    a = input()

    answer = ''
    stack = []
    for char in a:
        if char in cal:
            while stack and cal[stack[-1]] >= cal[char]:
                answer += stack.pop()
            stack.append(char)
        else:
            answer += char
            
    while stack:
        answer += stack.pop()

    print(f'#{tc}', answer)