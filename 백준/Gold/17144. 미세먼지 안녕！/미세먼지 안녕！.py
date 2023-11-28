'''
가로 세로 NxM 꼭 M으로 놔야해!!!!!!
돌풍이 방향을 꺾는 범위 잘못 지정 (0-robot/robot+1-N을 0-N으로 일괄 설정해버림)
di, dj도 좌우 반대로 적음 
new_arr 만들 때, 공청기 -1 설정 안 함
'''
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 공청기 찾기 (무조건 하난가? 그렇겟지?)
robot = 0
for i in range(2, N):
    if arr[i][0] == -1:
        robot = i
        break

di = (0, -1, 0, 1)
dj = (-1, 0, 1, 0)  # 좌 상 우 하
for tc in range(T):
    # [1] 먼지 확산
    new_arr = [[0] * M for _ in range(N)]
    new_arr[robot][0] = -1  # 공청기 -1로 두기
    new_arr[robot+1][0] = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:  # 먼지가 있으면 (공청기 제외)
                new_arr[i][j] += arr[i][j]
                blow = arr[i][j] // 5
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != -1:
                        new_arr[i][j] -= blow
                        new_arr[nr][nc] += blow

    arr = new_arr
    
    # [2-1] 위 청소
    d = 1
    cr, cc = robot - 1, 0
    nr, nc = robot - 2, 0
    while (nr, nc) != (robot, 0):
        arr[cr][cc] = arr[nr][nc]
        if not 0 <= nr + di[d] <= robot or not 0 <= nc + dj[d] < M:
            d = (d + 1) % 4
        cr, cc = nr, nc
        nr += di[d]
        nc += dj[d]
    arr[cr][cc] = 0

    # [2-2] 아래 청소
    d = 3
    cr, cc = robot + 2, 0
    nr, nc = robot + 3, 0
    while (nr, nc) != (robot + 1, 0):
        arr[cr][cc] = arr[nr][nc]
        if not robot < nr + di[d] < N or not 0 <= nc + dj[d] < M:
            d = (d - 1) % 4
        cr, cc = nr, nc
        nr += di[d]
        nc += dj[d]
    arr[cr][cc] = 0

answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            answer += arr[i][j]
print(answer)