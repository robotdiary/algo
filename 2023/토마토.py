from collections import deque
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
visited = set()
tomato = set()  # 안 익은 토마토
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
        # 안 익은 토마토 모음
        elif arr[i][j] == 0:
            tomato.add((i, j))

day = -1
while q:
    for _ in range(len(q)):
        cr, cc = q.popleft()
        for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                if arr[nr][nc] == 0:
                    q.append((nr, nc))
                    visited.add((nr, nc))
    else:
        day += 1

if visited != tomato:
    day = -1

print(day)