from collections import deque
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomatoes = deque()  # 익은 토마토 좌표
target = 0  # 안 익은 퇌토 수
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                tomatoes.append((i, j, k))
            elif arr[k][i][j] == 0:
                target += 1
answer = 0
while tomatoes and target:  # 안 익은 토마토가 있고 익힐 수 있는 토마토가 있으면
    for day in range(len(tomatoes)):
        cr, cc, ck = tomatoes.popleft()
        for dk, dr, dc in (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0):
            nk, nr, nc = ck + dk, cr + dr, cc + dc
            if 0 <= nk < h and 0 <= nr < n and 0 <= nc < m and arr[nk][nr][nc] == 0:
                arr[nk][nr][nc] = 1
                target -= 1
                tomatoes.append((nr, nc, nk))
    answer += 1
if not target:
    print(answer)
else:
    print(-1)