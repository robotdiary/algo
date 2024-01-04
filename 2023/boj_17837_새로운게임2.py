'''
현기증나요
빨간 바닥이랑 흰 바닥이 중복될 거라 함수로 빼두고 사용
놓쳤던 부분들 :
    체스판의 말만 옮기는 게 아니라, dict(번호: 위치)도 재설정 해줘야 함
    옮긴 말의 위치를 dict(번호: 위치)에 재설정할 때, 자신이면 방향이 바뀌었을 수 있음!
    red일 땐, 자신이 마지막에 나오고 white일 땐, 자신이 먼저 나온다 popleft와 pop
    if else가 반복되니까 머리가 빙글빙글 돈다
배울 점 :
    team으로부터 pop이나 popleft를 할 필요 없이 team을 잘 뽑아두고 arr[r][c]자체를 떼다가 붙여도 된다 lst + lst
'''
from collections import deque


def red(team, r, c, d):
    while len(team) > 1:
        current = team.popleft()
        visited[r][c].append(current)
        # 옮긴 모든 말들의 위치를 바꿔줘야 함
        horses[current] = (r, c, horses[current][2])
    current = team.popleft()
    visited[r][c].append(current)
    horses[current] = (r, c, d)
    return len(visited[nr][nc])


def white(team, r, c, d):
    current = team.pop()
    visited[r][c].append(current)
    horses[current] = (r, c, d)
    while team:
        current = team.pop()
        visited[r][c].append(current)
        horses[current] = (r, c, horses[current][2])
    return len(visited[r][c])


# [2] 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다.
def maketeam(r, c, num):
    team = deque()
    while visited[r][c][-1] != num:
        team.append(visited[r][c].pop())
    team.append(visited[r][c].pop())  # 본인 빼먹을 뻔했다
    return team


N, K = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]  # '0', '1', '2'
visited = [[[] for _ in range(N)] for _ in range(N)]  # 체스판

# [0] 게임은 체스판 위에 말 K개를 놓고 시작한다.
horses = {}
for idx in range(1, K + 1):
    r, c, d = map(lambda x:int(x) - 1, input().split())
    horses[idx] = (r, c, d)
    visited[r][c].append(idx)

di = (0, 0, -1, 1)
dj = (1, -1, 0, 0)  # 우 좌 상 하
oppo = {0: 1, 1: 0, 2: 3, 3: 2}
answer = 0
for tc in range(1, 1001):
    # [1] 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다.
    for horse in range(1, K + 1):
        cr, cc, direction = horses[horse]
        nr, nc = cr + di[direction], cc + dj[direction]
        # [3] 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르다.
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in {'0', '1'}:
            # [3-1] 이동하려는 칸이 흰생인 경우, 순서 그대로 이동
            if arr[nr][nc] == '0':
                if white(maketeam(cr, cc, horse), nr, nc, direction) >= 4:
                    answer = tc
                    break
            # [3-2] 이동하려는 칸이 빨강인 경우, 순서 바꿔서 이동
            elif arr[nr][nc] == '1':
                if red(maketeam(cr, cc, horse), nr, nc, direction) >= 4:
                    answer = tc
                    break
        # [3-3] 파란색인 경우나 체스판을 벗어나는 경우에는 이동 방향을 반대로 하고 한 칸 이동한다.
        else:
            direction = oppo[direction]
            nr, nc = cr + di[direction], cc + dj[direction]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in {'0', '1'}:
                if arr[nr][nc] == '0':
                    # [4] 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료
                    if white(maketeam(cr, cc, horse), nr, nc, direction) >= 4:
                        answer = tc
                        break
                elif arr[nr][nc] == '1':
                    if red(maketeam(cr, cc, horse), nr, nc, direction) >= 4:
                        answer = tc
                        break
            # 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
            else:
                horses[horse] = (cr, cc, direction)
    if answer:
        print(answer)
        break

else:
    print(-1)