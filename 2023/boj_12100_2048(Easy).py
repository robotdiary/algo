from collections import deque


def push(board):
    # 왼쪽으로 이동
    for rc in range(4):
        new_arr = [[0] * N for _ in range(N)]
        for i in range(N):
            # 시작점 설정
            cr, cc, idx = 0, 0, 0
            if rc == 0: cr, cc = i, 0
            elif rc == 2: cr, cc = 0, i
            elif rc == 1:
                cr, cc = i, N - 1
                idx = N - 1
            else:
                cr, cc = N - 1, i
                idx = N - 1

            while 0 <= cr < N and 0 <= cc < N:
                if board[cr][cc]:
                    if rc in [0, 1]:
                        new_arr[i][idx] = board[cr][cc]
                    else:
                        new_arr[idx][i] = board[cr][cc]
                    idx += dd[rc]
                cr += di[rc]
                cc += dj[rc]
        q.append(crush(new_arr, rc))
        # print(*new_arr, sep='\n')
        # print('===================')


def crush(board, rc):
    global answer
    mx = 0
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        # 시작점 설정
        cr, cc, idx = 0, 0, 0
        if rc == 0:
            cr, cc = i, 0
        elif rc == 2:
            cr, cc = 0, i
        elif rc == 1:
            cr, cc = i, N - 1
            idx = N - 1
        else:
            cr, cc = N - 1, i
            idx = N - 1

        while 0 <= cr + di[rc] < N and 0 <= cc + dj[rc] < N:
            if board[cr][cc]:
                if board[cr][cc] == board[cr + di[rc]][cc + dj[rc]]:
                    if rc in [0, 1]:
                        new_arr[i][idx] = board[cr][cc] + board[cr + di[rc]][cc + dj[rc]]
                        mx = max(mx, board[cr][cc] + board[cr + di[rc]][cc + dj[rc]])
                    else:
                        new_arr[idx][i] = board[cr][cc] + board[cr + di[rc]][cc + dj[rc]]
                        mx = max(mx, board[cr][cc] + board[cr + di[rc]][cc + dj[rc]])
                    idx += dd[rc]
                    cr += di[rc]
                    cc += dj[rc]
                else:
                    if rc in [0, 1]:
                        new_arr[i][idx] = board[cr][cc]
                        mx = max(mx, board[cr][cc])
                    else:
                        new_arr[idx][i] = board[cr][cc]
                        mx = max(mx, board[cr][cc])
                    idx += dd[rc]
            cr += di[rc]
            cc += dj[rc]
        if 0 <= cr < N and 0 <= cc < N:
            if rc in [0, 1]:
                new_arr[i][idx] = board[cr][cc]
                mx = max(mx, board[cr][cc])

            else:
                new_arr[idx][i] = board[cr][cc]
                mx = max(mx, board[cr][cc])
    answer = max(answer, mx)
    # print(*new_arr, sep='\n')
    # print('===================')
    return new_arr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)
dd = (1, -1, 1, -1)
day = 0
q = deque([arr])
answer = 0
while q and day < 5:
    for d in range(len(q)):
        # mx, cnt, board = q.popleft()
        push(q.popleft())
    else:
        day += 1
print(answer)