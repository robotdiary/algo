'''
총 풀이 시간 2시간 45분
20분 구상
55분 구현 → 런타임 에러 + tc5 틀림
60분 tc5가 도저히 손으로도 안 풀림
20분 문제를 계속 다시 읽고 혹시 하면서 여러가지 확인 후
     벽 치는 타이밍을 옮기고 성공

1차 : tc5 런타임 에러 꼭 불안한 부분이 틀리는 법
	 visited에 이전 좌표를 찍어뒀는데 돌이켜 찾아가는 부분이 굉장히 헷갈렸다.
	 결국엔 벽 때문에 길을 못 찾는 거였지만
	 visited[visited[result... 보다 덜 헷갈리고 가시적인 로직으로 변경했다.

2차 : 벽 설치 타이밍을 이해 못 해서 70분 동안 고민했다
	 너무 부분 부분 손봐서 이제 찝찝함 근데 지치니까 일단 제출하고 보자
	 시험이었다면 지쳐도 다시 전체적으로 훑어보고, 더 여러개의 tc로 확인해봤어야 함

아이디어1 모든 분신을 배열에 퍼뜨리면서 진행 -> 30명의 분신 너무 많지
아이디어2 턴마다 bfs를 돌아서 이동하기 -> 차라리 이걸 해보자
사람을 넣을 table[list]와 나중에 추가될 walls[]를 사용
'''
from collections import deque


def bfs(goal, sr, sc):  # 현재 위치에서 최소거리 다음 위치 찾기
    q = deque([(sr, sc)])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    rr, rc = sr, sc
    while q:
        cr, cc = q.popleft()
        for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == goal:
                    visited[nr][nc] = (cr, cc)
                    rr, rc = nr, nc
                    q = 0
                    break
                if arr[nr][nc] != -1:
                    visited[nr][nc] = (cr, cc)
                    q.append((nr, nc))

    path = []
    while True:
        path.append((rr, rc))
        if visited[visited[rr][rc][0]][visited[rr][rc][1]] == 1:
            break
        rr, rc = visited[rr][rc][0], visited[rr][rc][1]
    return path[-1]


def find_basecamp(gr, gc):
    q = deque([(gr, gc)])
    visited = [[0] * N for _ in range(N)]
    visited[gr][gc] = 1
    candidate = []
    while q and not candidate:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != -1:
                    if arr[nr][nc] == 1:
                        visited[nr][nc] = 1
                        candidate.append((nr, nc))
                    else:
                        visited[nr][nc] = 1
                        q.append((nr, nc))

    candidate.sort()
    return candidate[0]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 1:베이스캠프 / 2~: 목적지 / -1:벽
basecamp = []  # 베이스캠프를 찾을 목적지 좌표
for convi in range(2, M + 2):
    X, Y = map(lambda x: int(x) - 1, input().split())
    arr[X][Y] = convi
    basecamp.append((X, Y))
table = [[[] for _ in range(N)] for _ in range(N)]  # 사람 넣는다
players = 0
answer = 0
walls = []  # 턴이 끝난 후 벽이 될 위치
while players < M:
    # [1] 모두 이동
    move = []
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                for k in range(len(table[i][j])):
                    player = table[i][j].pop()  # 이동할 사람
                    nr, nc = bfs(player, i, j)  # 이동할 위치
                    move.append((player, nr, nc))

    for p, r, c in move:
        # [2] 편의점 도착시
        if arr[r][c] == p:
            walls.append((r, c))
            players += 1
        else:
            table[r][c].append(p)

    # 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
    for _ in range(len(walls)):
        wr, wc = walls.pop()
        arr[wr][wc] = -1

    # [3] 사람 추가
    if answer < M:
        mr, mc = find_basecamp(*basecamp[answer])  # 베이스 캠프 찾기
        table[mr][mc].append(answer + 2)  # 찾은 위치에 사람 추가
        walls.append((mr, mc))  # 베이스 캠프를 벽으로

    answer += 1

print(answer)

