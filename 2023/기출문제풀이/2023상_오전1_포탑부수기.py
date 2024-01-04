'''
1시간 30분 구현1시간 디버깅13분
공격자의 최근 공격 업데이트 까먹음
마지막 sort를 또 까먹었어
공격력을 -로 넣지 않음
N, M실수

레이저, 포탄 공격은 한 번에 잘 구현 했다
'''
from collections import deque


def attack(x, y, p, gx, gy):
    # 레이저 공격
    mini = p // 2
    q = deque([(x, y)])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = (-1, -1)
    group = {(gx, gy), (x, y)}
    while q:
        cr, cc = q.popleft()
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr, nc = cr + dr, cc + dc
            nr %= N
            nc %= M
            if visited[nr][nc] == 0 and arr[nr][nc] > 0:
                if (nr, nc) == (gx, gy):
                    arr[nr][nc] -= p
                    r, c = cr, cc
                    while visited[r][c] != (-1, -1):
                        group.add((r, c))
                        arr[r][c] -= mini
                        r, c = visited[r][c]
                    return group
                visited[nr][nc] = (cr, cc)
                q.append((nr, nc))
    # 포탄 공격
    arr[gx][gy] -= p
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1):
        nr, nc = gx + dr, gy + dc
        nr %= N
        nc %= M
        if (nr, nc) != (x, y):
            group.add((nr, nc))
            arr[nr][nc] -= mini
    return group


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
towers = []
acc = N + M
# [0] 타워 정보 넣어 놓기
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            towers.append((-arr[i][j], 0, (i + j), j, i))  # -공격력, 최근 공격, 행+열, 열, 행
towers.sort()

for tc in range(1, K + 1):
    # 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지됩니다.
    if len(towers) == 1:
        break

    # [1] 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정

    power, _, _, C, R = towers.pop()
    # 핸디캡이 적용되어 N+M만큼의 공격력이 증가
    power = -power + acc
    arr[R][C] = power  # 배열에 적용

    _, _, _, gc, gr = towers[0]
    enemy = attack(R, C, power, gr, gc)

    # 포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) not in enemy:
                arr[i][j] += 1
            else:
                if arr[i][j] < 0:
                    arr[i][j] = 0

    # -공격력, 최근공격, 행+열, 열, 좌표
    new_towers = []
    for k in range(len(towers)):
        공격력, 최근공격, 행열, 열, 행 = towers.pop()
        if arr[행][열]:
            new_towers.append((-arr[행][열], 최근공격, 행열, 열, 행))

    towers = new_towers
    towers.append((-arr[R][C], tc, R+C, C, R))
    towers.sort()

print(-towers[0][0])