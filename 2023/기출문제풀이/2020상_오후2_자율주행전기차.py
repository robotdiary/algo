'''
재도전 40분
손님 못 찾을 때 놓침
'''
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
R, C = map(lambda x: int(x) - 1, input().split())

goals = {}  # idx: 목적지
for idx in range(2, M + 2):
    X, Y, gx, gy = map(lambda x: int(x) - 1, input().split())
    arr[X][Y] = idx
    goals[idx] = (gx, gy)

alive = [1] * (M + 2)
alive[0], alive[1] = 0, 0
while K and sum(alive):
    b1, b2 = 0, 1  # 손님용 연료, 목적지 연료

    # [1] 손님~
    guest = (N, N, 0)  # 좌표, 사람
    if arr[R][C] > 1:
        guest = (R, C, arr[R][C])
    else:
        q = deque([(R, C)])
        visited = [[0] * N for _ in range(N)]
        visited[R][C] = 1
        while q and not guest[2]:
            for day in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                        if arr[nr][nc] > 1:
                            guest = min(guest, (nr, nc, arr[nr][nc]))
                            visited[nr][nc] = 1
                        else:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
            else:
                b1 += 1
    if guest[0] == N:
        K = -1
        break
    R, C = guest[0], guest[1]
    alive[guest[2]] = 0
    arr[R][C] = 0

    K -= b1
    if K < 1:
        K = -1
        break

    # [2] 도착했습니다요~
    q = deque([(R, C)])
    visited = [[0] * N for _ in range(N)]
    visited[R][C] = 1
    flag = 0
    while q:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                    if (nr, nc) == goals[guest[2]]:
                        R, C = nr, nc
                        q = 0
                        flag = 1
                        break
                    q.append((nr, nc))
                    visited[nr][nc] = 1
            if flag:
                break
        else:
            b2 += 1
    K -= b2
    if not flag or K < 0:
        K = -1
        break
    K += b2 * 2

print(K)
