'''
공간 꽉 채워서 머리와 꼬리가 이어진 경우 틀림
기본 구상 로직이 너무 허술하다
'''
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
teams = {}
# 우선, 팀 dict를 들면서 번호를 팀이름(5번부터)으로 바꿔쓴다
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            num = len(teams) + 5
            stack = [(i, j)]
            team = deque([(i, j)])
            arr[i][j] = num
            tail = ()
            while stack:
                cr, cc = stack.pop()
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 2:
                            team.append((nr, nc))
                            stack.append((nr, nc))
                            arr[nr][nc] = num
                        elif arr[nr][nc] == 3:
                            tail = (nr, nc)
                            arr[nr][nc] = num
            team.append(tail)
            teams[num] = team

di = (0, -1, 0, 1)
dj = (1, 0, -1, 0)
direction = 0
answer = 0
for tc in range(K):
    # [1] 이동
    for t in teams:
        last = teams[t].pop()
        # 맨 뒤녀석 빼고 4로 변경
        arr[last[0]][last[1]] = 4
        # 1번 사람 추가
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = teams[t][0][0] + dr, teams[t][0][1] + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 4:
                arr[nr][nc] = t
                teams[t].appendleft((nr, nc))
                break

    # [2] 공 던지기

    # [2-1] 공 던지는 방향
    d = (direction + (tc // N)) % 4
    # [2-1] 공 시작점
    cal = tc % N
    if d == 0:
        cr, cc = cal, 0
    elif d == 1:
        cr, cc = N-1, cal
    elif d == 2:
        cr, cc = N-1 - cal, N-1
    else:
        cr, cc = 0, N-1 - cal
    # [2-2] 공 이동하면서 사람 찾기
    while 0 <= cr < N and 0 <= cc < N and arr[cr][cc] < 5:
        cr += di[d]
        cc += dj[d]
    if 0 <= cr < N and 0 <= cc < N and arr[cr][cc] > 4:
        answer += (teams[arr[cr][cc]].index((cr, cc)) + 1) ** 2
        teams[arr[cr][cc]].reverse()

print(answer)