from collections import defaultdict


def solve(x, y, d):
    acc = 0
    cr, cc = x, y
    while True:
        # 범위 밖이거나, 1-5 블럭이면 점수를 얻고 방향 전환
        nr, nc = cr + di[d], cc + dj[d]
        if not 0 <= nr < N or not 0 <= nc < N:
            acc += 1
            d = (d + 2) % 4
            nr, nc = cr, cc
            if 1 <= arr[nr][nc] <= 5:
                acc += 1
                d = oppo[arr[nr][nc]][d]
            elif 5 < arr[nr][nc]:
                nr, nc = wormholes[(nr, nc)]
        elif 1 <= arr[nr][nc] <= 5:
            acc += 1
            d = oppo[arr[nr][nc]][d]
        elif 5 < arr[nr][nc]:
            nr, nc = wormholes[(nr, nc)]
        cr, cc = nr, nc
        if arr[cr][cc] == -1 or (cr, cc) == (x, y):
            return acc


di = (-1, 0, 1, 0)  # 상 우 하 좌
dj = (0, 1, 0, -1)
oppo = {1: {0: 2, 1: 3, 2: 1, 3: 0}, 2: {0: 1, 1: 3, 2: 0, 3: 2}, 3 : {0: 3, 1: 2, 2: 0, 3: 1}, 4 : {0: 2, 1: 0, 2: 3, 3: 1}, 5 : {0: 2, 1: 3, 2: 0, 3: 1}}
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    defaultwormhole = defaultdict(list)
    wormholes = {}
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                defaultwormhole[arr[i][j]].append((i, j))
    for key in defaultwormhole:
        wormholes[defaultwormhole[key][0]] = defaultwormhole[key][1]
        wormholes[defaultwormhole[key][1]] = defaultwormhole[key][0]

    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for k in range(4):
                    answer = max(answer, solve(i, j, k))

    print(f'#{tc} {answer}')