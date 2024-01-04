from collections import deque


def bfs(r, c, k):
    q = deque([(r, c)])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    time = 1
    while q and time < k:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if not 0 <= nr < N or not 0 <= nc < N or arr[nr][nc] == '#':
                    return False
                if visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        else:
            time += 1
    return True


N = int(input())
arr = [list(input()) for _ in range(N)]

# [0] 시작 위치 찾기
sr, sc = -1, -1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            sr, sc = i, j
            arr[i][j] = '.'

# [1] 턴
q = deque([(sr, sc, 1)])  # 좌표, 크기
turn = 0
while q:
    for day in range(len(q)):
        cr, cc, size = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '.':
                if bfs(nr, nc, size + 1):
                    q.append((nr, nc, size + 1))
    else:
        turn += 1

print(turn)
