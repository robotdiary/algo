'''
플이시간 1시간 30분 : 구상-10분 / [1]까지구현-38분 / 나머지구현-28분 / 디버깅-18분
벽 좌표 -1로 받을 때, 방향도 -1 되어서 잘못 저장 되었다.
'''
from collections import deque


def check():
    for i, j in rooms:
        if arr[i][j] < K:
            return False
    return True


def make_wind():
    for ar, ac, ad in aircon:
        ar, ac = ar + di[ad], ac + dj[ad]
        visited = [[0] * N for _ in range(N)]
        visited[ar][ac] = 5
        q = deque([(ar, ac)])
        while q:
            cr, cc = q.popleft()
            if visited[cr][cc] == 1:
                break
            if (cr, cc, ad) not in walls:
                nr, nc = cr + di[ad], cc + dj[ad]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] - 1
                    q.append((nr, nc))
            nd = (ad + 1) % 4
            if (cr, cc, nd) not in walls and (cr + di[nd], cc + dj[nd], ad) not in walls:
                nr, nc = cr + di[nd] + di[ad], cc + dj[nd] + dj[ad]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] - 1
                    q.append((nr, nc))
            nd = (ad - 1) % 4
            if (cr, cc, nd) not in walls and (cr + di[nd], cc + dj[nd], ad) not in walls:
                nr, nc = cr + di[nd] + di[ad], cc + dj[nd] + dj[ad]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] - 1
                    q.append((nr, nc))

        for i in range(N):
            for j in range(N):
                plus[i][j] += visited[i][j]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
walls = set()
for _ in range(M):
    X, Y, S = map(lambda x: int(x) - 1, input().split())  # 0위 1왼 벽
    if S:
        walls.add((X, Y, 1))
        walls.add((X-1, Y, 3))
    else:
        walls.add((X, Y, 0))
        walls.add((X, Y-1, 2))

rooms = []
aircon = []
# [0] 위치 찾고 0으로 초기화
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            rooms.append((i, j))
            arr[i][j] = 0
        elif arr[i][j]:
            aircon.append((i, j, arr[i][j]-2))
            arr[i][j] = 0

di = (0, -1, 0, 1)
dj = (-1, 0, 1, 0)  # 좌, 상, 우, 하

# 에어컨에서 나오는 바람 미리 만들어두기
plus = [[0] * N for _ in range(N)]
make_wind()

for tc in range(100):
    if check():
        print(tc)
        break

    # [1] 에어컨 바람 불기
    for i in range(N):
        for j in range(N):
            arr[i][j] += plus[i][j]

    # [2] 섞이기
    new_arr = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            target = arr[i][j]
            for d in range(2, 4):
                if (i, j, d) in walls:
                    continue
                nr, nc = i + di[d], j + dj[d]
                if 0 <= nr < N and 0 <= nc < N:
                    cha = abs(target - arr[nr][nc]) // 4
                    if arr[nr][nc] < target:
                        new_arr[i][j] -= cha
                        new_arr[nr][nc] += cha
                    elif arr[nr][nc] > target:
                        new_arr[i][j] += cha
                        new_arr[nr][nc] -= cha

    # [3] 외벽에 있는 칸에 대해서만 시원함이 1씩 감소합니다.
    for i in range(N):
        if new_arr[0][i]:
            new_arr[0][i] -= 1
        if new_arr[-1][i]:
            new_arr[-1][i] -= 1
    for i in range(1, N-1):
        if new_arr[i][0]:
            new_arr[i][0] -= 1
        if new_arr[i][-1]:
            new_arr[i][-1] -= 1

    arr = new_arr
else:
    print(-1)
