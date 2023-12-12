from collections import deque
import sys
input = sys.stdin.readline

def bfs(q):
    visited = [[0] * n for _ in range(n)]
    eat = []
    acc = 1
    while q:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                    if 0 < arr[nr][nc] < size:
                        eat.append((nr, nc))
                        visited[nr][nc] = 1
                    elif arr[nr][nc] <= size:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
        if eat:
            return min(eat), acc  # 좌표, 거리
        acc += 1
    return False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
shark = (0, 0)
size = 2
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark = (i, j)
            arr[i][j] = 0

while True:
    fish = bfs(deque([shark]))
    if fish:
        frfc, distance = fish
        shark = (frfc[0], frfc[1])
        answer += distance
        arr[frfc[0]][frfc[1]] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    else:
        print(answer)
        break
