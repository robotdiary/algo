n, m, t = map(int, input().split())
arr = {0: [list(map(int, input().split())) for _ in range(n)], 1: [[0] * m for _ in range(n)]}
machine = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# [0] 공청기 위치 찾기
for i in range(2, n - 1):
    if arr[0][i][0] == -1:
        machine.append((i, 0))
        machine.append((i + 1, 0))
        arr[0][i][0] = 0              # 공청기 위치 0으로 변경
        arr[0][i + 1][0] = 0
        break

for tc in range(t):
    me = tc % 2
    you = (tc + 1) % 2

    # [1] 확산
    for i in range(n):
        for j in range(m):
            if arr[me][i][j]:
                acc = 0
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in machine:  # 공청기로 가면 안 돼
                        arr[you][nr][nc] += arr[me][i][j] // 5
                        acc += arr[me][i][j] // 5
                arr[you][i][j] += arr[me][i][j] - acc
                arr[me][i][j] = 0

    # [2-1] 위쪽 순환
    d = 0
    cr, cc = machine[0][0] - 1, 0
    while d < 4:
        nr, nc = cr + di[d], cc + dj[d]
        # print(nr, nc)
        if 0 <= nr <= machine[0][0] and 0 <= nc < m:
            arr[you][cr][cc] = arr[you][nr][nc]
            cr, cc = nr, nc
        else:
            d += 1
    # [2-2] 아래쪽 순환
    d -= 1
    cr, cc = machine[1][0] + 1, 0
    while d >= -1:
        nr, nc = cr + di[d], cc + dj[d]
        if machine[1][0] <= nr < n and 0 <= nc < m:
            arr[you][cr][cc] = arr[you][nr][nc]
            cr, cc = nr, nc
        else:
            d -= 1

answer = 0
last = t % 2
for i in range(n):
    answer += sum(arr[last][i])
print(answer)