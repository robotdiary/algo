'''
3시 33분 - 4시
불안해하면서 제출하게 된다.
'''
from collections import deque
N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]  # '2'불, '1'벽, '0'빈칸

fires = []
rooms = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '2':
            fires.append((i, j))
        elif arr[i][j] == '0':
            rooms.append((i, j))
answer = 0  # 최대값 잘못 설정


def comb():
    for i in range(len(rooms)):
        for j in range(i + 1, len(rooms)):
            for k in range(j + 1, len(rooms)):
                bfs([rooms[i], rooms[j], rooms[k]])


def bfs(lst):
    global answer
    cnt = len(rooms) - 3
    q = deque(fires)
    visited = [[0] * M for _ in range(N)]
    for r, c in fires:
        visited[r][c] = 1
    while q:
        cr, cc = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == '0' and (nr, nc) not in lst:
                    cnt -= 1
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    if cnt <= answer:
                        return
    answer = cnt


comb()
print(answer)
