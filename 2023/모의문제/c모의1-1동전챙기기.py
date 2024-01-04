from collections import deque


def solve(x, y, me):
    q = deque([(x, y)])  # 좌표
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    move = 0
    while q:
        move += 1
        for day in range(len(q)):
            cr, cc = q.popleft()
            for d in range(4):
                nr, nc = cr + di[d], cc + dj[d]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != '#':
                    if arr[nr][nc] != '.' and arr[nr][nc] > me:
                        dist[me][arr[nr][nc]] = move
                    q.append((nr, nc))
                    visited[nr][nc] = 1


def cur(depth, acc, start, coins):
    global answer
    if depth == 3:
        if dist[coins[-1]][-1] > 0:
            acc += dist[coins[-1]][-1]
            answer = min(answer, acc)
        return

    if acc >= answer:
        return

    for i in range(start, 10):
        if i in dist.keys():
            if dist[coins[-1]][i] > 0:
                cur(depth + 1, acc + dist[coins[-1]][i], i + 1, coins + [i])


N = int(input())
arr = [list(input()) for _ in range(N)]  # '#'벽 '.'빈칸 'S'시작 'E'도착 '1'-'9'동전

# [0] 시작점 도착점 찾고 '.'로 바꾸기
sr, sc = -1, -1
gr, gc = -1, -1
info = {}  # 동전 : 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            sr, sc = i, j
            arr[i][j] = '.'
            info[0] = (i, j)
        elif arr[i][j] == 'E':
            gr, gc = i, j
        elif arr[i][j] not in ['#', '.']:
            arr[i][j] = int(arr[i][j])
            info[arr[i][j]] = (i, j)

coin_cnt = len(info)
arr[gr][gc] = 10
info[arr[gr][gc]] = (gr, gc)

di = (1, 0, -1, 0)
dj = (0, 1, 0, -1)

dist = {key: [-1] * 11 for key in info}

# [1] 서로 서로 거리 구하기
for i in range(10):
    if i in info:
        solve(*info[i], i)

# [2] 동전 세개 고르기
answer = 999999
cur(0, 0, 1, [0])

if answer == 999999:
    answer = -1
print(answer)