def dfs(depth, acc, cr, cc, visited):
    global answer
    if depth == 3:
        answer = max(answer, acc)
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and (nr, nc) not in visited:
            dfs(depth + 1, acc + arr[nr][nc], nr, nc, visited | {(nr, nc)})


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        dfs(0, arr[i][j], i, j, {(i, j)})
        arr[i][j] = 0
print(answer)