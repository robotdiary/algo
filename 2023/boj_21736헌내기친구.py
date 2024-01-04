n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

stack = []
for i in range(n):
    if 'I' in arr[i]:
        stack.append((i, arr[i].index('I')))
answer = 0
visited = set(stack[0])

while stack:
    cr, cc = stack.pop()
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and arr[nr][nc] != 'X':
            if arr[nr][nc] == 'P':
                answer += 1
            stack.append((nr, nc))
            visited.add((nr, nc))

if answer:
    print(answer)
else:
    print('TT')