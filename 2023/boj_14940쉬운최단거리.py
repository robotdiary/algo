from collections import deque
n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
# 0벽 1통로 2목적지
stack = deque()
for i in range(n):
    if '2' in arr[i]:
        stack.append((i, arr[i].index('2'), 0))
        arr[i][arr[i].index('2')] = 0

visited = {(stack[0])}
while stack:
    cr, cc, cnt = stack.popleft()
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and arr[nr][nc] == '1':
            arr[nr][nc] = cnt + 1
            stack.append((nr, nc, cnt + 1))
            visited.add((nr, nc))

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            arr[i][j] = -1
        elif arr[i][j] == '0':
            arr[i][j] = 0

for i in range(n):
    print(*arr[i])