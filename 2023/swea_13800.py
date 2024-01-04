n = int(input())
lst = list(map(int, input().split()))

stack = []  # 층수와 건물번호 필요
answer = []
for i in range(n):  # 건물 번호는 i + 1
    while stack:
        if stack[-1][0] < lst[i]:
            stack.pop()
        else:
            answer.append(stack[-1][1])
            stack.append((lst[i], i + 1))
            break
    else:
        answer.append(0)
        stack.append((lst[i], i + 1))
print(*answer)