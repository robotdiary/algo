'''
12:39 - 12:55
visited 봐야하는데 또 arr을 봤네
이미 병원인 곳은 바이러스가 없음을 간과
'''
from collections import deque


def bfs(q):
    visited = [[0] * N for _ in range(N)]
    time = 1
    cnt = virus
    while q:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                    if arr[nr][nc] == 0:
                        cnt -= 1
                        if not cnt:
                            return time
                    visited[nr][nc] = 1
                    q.append((nr, nc))
        else:
            time += 1
            if time >= answer:
                return 99999999
    return 99999999


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# [0] 병원 찾기
hosp = []
virus = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            hosp.append((i, j))
            arr[i][j] = -1
        elif arr[i][j] == 0:
            virus += 1

if not virus:
    print(0)
else:
    answer = 99999999
    # [1] M개의 병원 고르기
    for i in range(1 << len(hosp)):
        selected = []
        for j in range(len(hosp)):
            if i & (1 << j):
                selected.append(hosp[j])
        # [2] 바이러스 없애기
        if len(selected) == M:
            answer = min(answer, bfs(deque(selected)))

    if answer == 99999999:
        print(-1)
    else:
        print(answer)