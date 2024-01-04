from collections import deque


def dfs(stack):
    lines = set()
    while stack:
        cr, cc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n and island[nr][nc] == 0:
                if arr[nr][nc] == '1':
                    island[nr][nc] = sea
                    stack.append((nr, nc))
                else:
                    lines.add((cr, cc))

    bfs(deque(lines))


def bfs(q):
    global answer
    visited = [[0] * n for _ in range(n)]
    length = 0
    while q:
        for l in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                    if arr[nr][nc] == '1' and island[nr][nc] != sea:
                        answer = min(answer, length)
                        return
                    elif arr[nr][nc] == '0':
                        q.append((nr, nc))
                        visited[nr][nc] = 1
        length += 1


n = int(input())
arr = [list(input().split()) for _ in range(n)]  # 문자열
island = [[0] * n for _ in range(n)]  # 바다를 1, 2, 3으로 적자
sea = 1
answer = 987654321
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and island[i][j] == 0:
            island[i][j] = sea
            dfs([(i, j)])
            sea += 1

print(answer)