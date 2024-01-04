'''
구현 25분 디버깅 15분
arr []로 만들어야하는데 0으로 만들어놨네
lst.index(p) 값 없는 ValueError
범위 설정 한 번 더 해줘야 함

범위 밖 & 파랑을 먼저 처리해주니까 훨씬 깔끔하게 끝났다. (코드 길이도, 시간도, 메모리도)
'''


def white(x, y, nx, ny, p):
    idx = arr[x][y].index(p)
    length = len(arr[nx][ny])
    acc = len(arr[x][y][idx:])
    if length + acc >= 4:
        return True
    arr[nx][ny] += arr[x][y][idx:]
    arr[x][y] = arr[x][y][:idx]
    for k in arr[nx][ny][length:]:
        mal[k][0] = nx
        mal[k][1] = ny
    return False


def red(x, y, nx, ny, p):
    idx = arr[x][y].index(p)
    length = len(arr[nx][ny])
    acc = len(arr[x][y][idx:])
    if length + acc >= 4:
        return True
    arr[nx][ny] += arr[x][y][idx:][::-1]
    arr[x][y] = arr[x][y][:idx]
    for k in arr[nx][ny][length:]:
        mal[k][0] = nx
        mal[k][1] = ny
    return False


N, K = map(int, input().split())
table = [list(input().split()) for _ in range(N)]  # '0'흰 '1'빨 '2'파
arr = [[[] for _ in range(N)] for _ in range(N)]
mal = {}
for idx in range(1, K + 1):
    X, Y, D = map(lambda x: int(x) - 1, input().split())
    mal[idx] = [X, Y, D]
    arr[X][Y].append(idx)
di = (0, 0, -1, 1)
dj = (1, -1, 0, 0)
oppo = {0: 1, 1: 0, 2: 3, 3: 2}

flag = 0
for turn in range(1, 1001):
    # [1] 1번 말부터 k번 말까지 규칙대로 순서대로 움직입니다.
    for player in range(1, K + 1):
        cr, cc, d = mal[player]
        nr, nc = cr + di[d], cc + dj[d]
        # [1] 칸이 파란색일 경우
        if not 0 <= nr < N or not 0 <= nc < N or table[nr][nc] == '2':
            d = oppo[d]
            mal[player][2] = d
            nr, nc = cr + di[d], cc + dj[d]
        if 0 <= nr < N and 0 <= nc < N:  # 범위 한 번 더 봐줘야 함
            if table[nr][nc] == '0':
                if white(cr, cc, nr, nc, player):
                    flag = 1
                    break
            elif table[nr][nc] == '1':
                if red(cr, cc, nr, nc, player):
                    flag = 1
                    break

    if flag:
        print(turn)
        break
else:
    print(-1)

