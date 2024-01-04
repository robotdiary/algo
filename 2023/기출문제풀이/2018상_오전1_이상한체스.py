'''
4시 55분 - 5시 30분
가지치기 모르겠다 -> 그치만 배열이 8x8, 체스말도 8개 뿐이니까 그냥 해
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 6벽

mal = {1: [[0], [1], [2], [3]],
       2: [(0, 2), (1, 3)],
       3: [(0, 1), (1, 2), (2, 3), (3, 0)],
       4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
       5: [(0, 1, 2, 3)]}

di = (-1, 0, 1, 0)  # 상 우 하 좌
dj = (0, 1, 0, -1)

rooms = set()  # 빈 방
board = []  # 내 체스말
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            rooms.add((i, j))
        elif arr[i][j] < 6:
            board.append((arr[i][j], i, j))


def cur(depth, visited):
    global answer
    if depth == len(board):
        answer = min(answer, len(rooms - visited))
        return

    for dest in mal[board[depth][0]]:
        cr, cc = board[depth][1], board[depth][2]
        visit = set()
        for nd in dest:
            nr, nc = cr + di[nd], cc + dj[nd]
            while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 6:
                visit.add((nr, nc))
                nr += di[nd]
                nc += dj[nd]
        cur(depth + 1, visited | visit)


answer = len(rooms)
cur(0, set())
print(answer)
