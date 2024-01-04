'''
총 풀이시간 : 2시간 10분
20분 : 구상
70분 : [1] 구현
15분 : 나머지 구현
25분 : tc가 틀려서 문제와 다르게 구현한 부분 찾아서 제출

[3] 온도가 있는 곳의 바깥이 아니라 방의 바깥 쪽이 줄어드는 거였다
[2] 온도 있는 곳만 돌지 말고 전체를 돌며서 조절하는 거여 이녀석아~

다른 사람들의 온풍기 퍼지는 부분 코드 보기, 다시 풀 땐 [1]의 구현 시간을 좀 줄여보자
'''
from collections import deque


def refresh():
    for r, c, d in air:
        nr, nc = r + di[d], c + dj[d]
        q = deque([(nr, nc)])
        visited = [[0] * C for _ in range(R)]
        arr[nr][nc] += 5
        visited[nr][nc] = 1
        for plus in range(4, 0, -1):
            for day in range(len(q)):
                cr, cc = q.popleft()
                # 세 방향 확인
                if 0 <= cr + di[d] < R and 0 <= cc + dj[d] < C:
                    if d not in walls[cr][cc] and visited[cr + di[d]][cc + dj[d]] == 0:
                        arr[cr + di[d]][cc + dj[d]] += plus
                        q.append((cr + di[d], cc + dj[d]))
                        visited[cr + di[d]][cc + dj[d]] = 1
                if d in [1, 2]:
                    # 아래 / 옆
                    dr = cr + 1
                    if 0 <= dr < R and 0 <= cc < C and 4 not in walls[cr][cc]:
                        if 0 <= dr + di[d] < R and 0 <= cc + dj[d] < C:
                            if d not in walls[dr][cc] and visited[dr + di[d]][cc + dj[d]] == 0:
                                arr[dr + di[d]][cc + dj[d]] += plus
                                q.append((dr + di[d], cc + dj[d]))
                                visited[dr + di[d]][cc + dj[d]] = 1
                    # 위 / 옆
                    dr = cr - 1
                    if 0 <= dr < R and 0 <= cc < C and 3 not in walls[cr][cc]:
                        if 0 <= dr + di[d] < R and 0 <= cc + dj[d] < C:
                            if d not in walls[dr][cc] and visited[dr + di[d]][cc + dj[d]] == 0:
                                arr[dr + di[d]][cc + dj[d]] += plus
                                q.append((dr + di[d], cc + dj[d]))
                                visited[dr + di[d]][cc + dj[d]] = 1
                else:
                    # 오른 / 옆
                    dc = cc + 1
                    if 0 <= cr < R and 0 <= dc < C and 1 not in walls[cr][cc]:
                        if 0 <= cr + di[d] < R and 0 <= dc + dj[d] < C:
                            if d not in walls[cr][dc] and visited[cr + di[d]][dc + dj[d]] == 0:
                                arr[cr + di[d]][dc + dj[d]] += plus
                                q.append((cr + di[d], dc + dj[d]))
                                visited[cr + di[d]][dc + dj[d]] = 1
                    # 왼 / 옆
                    dc = cc - 1
                    if 0 <= cr < R and 0 <= dc < C and 2 not in walls[cr][cc]:
                        if 0 <= cr + di[d] < R and 0 <= dc + dj[d] < C:
                            if d not in walls[cr][dc] and visited[cr + di[d]][dc + dj[d]] == 0:
                                arr[cr + di[d]][dc + dj[d]] += plus
                                q.append((cr + di[d], dc + dj[d]))
                                visited[cr + di[d]][dc + dj[d]] = 1


def 온도조절():
    board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # if arr[i][j]: 이게 아니지
            for direction in [1, 4]:  # 중복으로 깎아버려씀
                nr, nc = i + di[direction], j + dj[direction]
                if 0 <= nr < R and 0 <= nc < C and direction not in walls[i][j]:
                    cha = abs(arr[i][j] - arr[nr][nc]) // 4
                    if cha:
                        if arr[i][j] > arr[nr][nc]:
                            board[i][j] -= cha
                            board[nr][nc] += cha
                        else:
                            board[nr][nc] -= cha
                            board[i][j] += cha
    for i in range(R):
        for j in range(C):
            arr[i][j] += board[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0


def 바깥온도감소():
    for i in range(1, R-1):
        if arr[i][0]:
            arr[i][0] -= 1
        if arr[i][C-1]:
            arr[i][C-1] -= 1
    for i in range(C):
        if arr[0][i]:
            arr[0][i] -= 1
        if arr[R-1][i]:
            arr[R-1][i] -= 1


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
k = []  # 조사할 칸
air = []  # 온풍기 위치, 방향
for i in range(R):
    for j in range(C):
        if arr[i][j] == 5:
            k.append((i, j))
            arr[i][j] = 0
        elif arr[i][j]:
            air.append((i, j, arr[i][j]))
            arr[i][j] = 0

walls = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(int(input())):
    X, Y, T = map(int, input().split())
    X -= 1
    Y -= 1
    if T:
        walls[X][Y].append(1)  # 가로
        walls[X][Y + 1].append(2)  # 가로
    else:
        walls[X][Y].append(3)  # 세로
        walls[X-1][Y].append(4)  # 세로
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0] # 없음, 우, 좌, 상, 하

for choco in range(1, 101):
    # [1] 바람 나오기
    refresh()
    # [2] 온도 조절
    온도조절()
    # [3] 바깥 온도 감소
    바깥온도감소()
    # [4] 조사칸 확인
    for n, m in k:
        if arr[n][m] < K:
            break
    else:
        print(choco)
        break

else:
    print(101)