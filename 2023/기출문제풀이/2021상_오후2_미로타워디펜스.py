'''
구멍 찾음 : 구슬 셀 때, 맨 마지막으로 센 구슬은 카운트가 안 된다
달라지는 것으로 카운트할 땐, 항상 마지막 걸 확인!!!
'''
def make_snail():
    cr, cc, d = middle, middle, 2
    visited = [[0] * N for _ in range(N)]
    visited[cr][cc] = (middle, middle)
    while True:
        nr, nc = cr + di[d], cc + dj[d]
        if 0 <= nr < N and 0 <= nc < N:
            visited[nr][nc] = (cr, cc)
            cr, cc = nr, nc
            nd = (d - 1) % 4
            if visited[cr + di[nd]][cc + dj[nd]] == 0:
                d = nd
        else:
            break
    # print(*visited, sep='\n')
    return visited


def move():
    d = 0
    cr, cc = middle+1, middle-1
    for i in range(1, len(go)):
        for g in range(go[i]):
            mr, mc = cr, cc
            while arr[snail[mr][mc][0]][snail[mr][mc][1]] == 0:
                arr[mr][mc], arr[snail[mr][mc][0]][snail[mr][mc][1]] = arr[snail[mr][mc][0]][snail[mr][mc][1]], arr[mr][mc]
                mr, mc = snail[mr][mc][0], snail[mr][mc][1]

            cr, cc = cr + di[d], cc + dj[d]

        else:
            d = (d - 1) % 4


def crush():
    global answer
    d = 1
    cr, cc = middle, middle - 1
    target = -1
    cnt = []
    flag = True
    for i in range(len(go)):
        for g in range(go[i]):
            if arr[cr][cc] == target:
                cnt.append((cr, cc))
            else:
                if len(cnt) >= 4:
                    answer += target * len(cnt)
                    flag = False
                    for r, c in cnt:
                        arr[r][c] = 0
                target = arr[cr][cc]
                cnt = [(cr, cc)]
            cr, cc = cr + di[d], cc + dj[d]

        else:
            d = (d - 1) % 4

    return flag


def make_arr():
    d = 0
    cr, cc = middle + 1, middle - 1
    target = arr[middle][middle-1]
    cnt = 1
    lst = []
    for i in range(1, len(go)):
        for g in range(go[i]):
            if arr[cr][cc] == target:
                cnt += 1
            else:
                lst.append(cnt)
                lst.append(target)
                target = arr[cr][cc]
                cnt = 1
            cr, cc = cr + di[d], cc + dj[d]

        else:
            d = (d - 1) % 4

    new_arr = [[0] * N for _ in range(N)]
    new_arr[middle][middle] = '1'
    d = 1
    cr, cc = middle, middle - 1
    idx = 0
    for i in range(len(go)):
        for g in range(go[i]):
            new_arr[cr][cc] = lst[idx]
            idx += 1
            if idx >= len(lst):
                return new_arr
            cr, cc = cr + di[d], cc + dj[d]

        else:
            d = (d - 1) % 4

    return new_arr


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
players = list(tuple(map(int, input().split())) for _ in range(M))

middle = N//2
arr[middle][middle] = '1'
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)  # 우, 하, 좌, 상
snail = make_snail()
go = [i // 2 for i in range(3, N * 2)] + [N-1]
answer = 0
for turn in range(M):
    # [1] 공격
    D, P = players[turn]
    for attack in range(1, P + 1):
        answer += arr[middle + (di[D] * attack)][middle + (dj[D] * attack)]
        arr[middle + (di[D] * attack)][middle + (dj[D] * attack)] = 0

    # [2] 앞으로 이동
    while True:
        move()
        # print(*arr, sep='\n')
        # print()
        if crush():
            break
        move()

    # [3] 새 배열 만들기
    arr = make_arr()
    # print(*arr, sep='\n')
print(answer)