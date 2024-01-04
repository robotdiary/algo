'''
1시간 30분 첫구현-50분 틀림
info 바로 바로 바꿔준다면서 또 방향만 기억해서 바꿔주고 위치는 안 바꿔줬다.
테이블과 인포를 동시에 바꾸는 걸 기억해야함!
그리고 미리 원래 자리에서 빼고 넣기 주의하기

로직 틀린 건 방향을 돌면서 위치를 찾을 때, 찾았으면 break를 걸어서 멈춰줘야지
'''


def change_gun(x, y, g, me):
    if arr[x][y]:
        arr[x][y].sort()
        if g == 0:
            g = arr[x][y].pop()
            players[me][4] = g
        elif arr[x][y][-1] > g:
            g, arr[x][y][-1] = arr[x][y][-1], g
            players[me][4] = g  # 여기도 무조건 하는 걸로 바꾸고, lose에서 총 0으로 안 해도 될 듯
    return g


def fight(me, you, x, y):
    me_power = players[me][3] + players[me][4]
    you_power = players[you][3] + players[you][4]
    winner = me
    loser = you
    result = me_power - you_power

    if me_power < you_power:
        winner, loser, result = you, me, you_power - me_power
    elif me_power == you_power and players[me][3] < players[you][3]:
        winner, loser, result = you, me, you_power - me_power

    lose(loser, x, y)
    win(winner, result, x, y)


def lose(man, x, y):
    mr, mc, md, ms, mg = players[man]
    if mg:
        arr[x][y].append(mg)  # arr을 table이라고 적음
        players[man][4] = 0
    for nd in range(4):
        mnr, mnc = mr + di[(md+nd)% 4], mc + dj[(md+nd)% 4]
        if 0 <= mnr < N and 0 <= mnc < N and table[mnr][mnc] == 0:
            table[mnr][mnc] = man
            players[man][0] = mnr
            players[man][1] = mnc
            players[man][2] = (md+nd) % 4
            change_gun(mnr, mnc, 0, man)
            break   # 왜 안 멈췄어


def win(man, score, x, y):
    global answer
    answer[man] += score
    change_gun(x, y, players[man][4], man)
    table[x][y] = man
    players[man][0], players[man][1] = x, y


N, M, K = map(int, input().split())
arr = [list(map(lambda x:[int(x)], input().split())) for _ in range(N)]
players = {}
table = [[0]*N for _ in range(N)]
for idx in range(1, M+1):
    X, Y, D, S = map(int, input().split())
    X -= 1
    Y -= 1
    table[X][Y] = idx
    players[idx] = [X, Y, D, S, 0]  # 좌표, 방향, 힘, 총


di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)  # 상 우 하 좌
answer = [0] * (M + 1)
for tc in range(K):
    for player in range(1, M + 1):
        cr, cc, d, power, gun = players[player]

        table[cr][cc] = 0  # 자리 빼라 이녀석아

        if not 0 <= cr + di[d] < N or not 0 <= cc + dj[d] < N:
            players[player][2] = (d + 2) % 4
            d = (d + 2) % 4
        nr, nc = cr + di[d], cc + dj[d]

        players[player][0], players[player][1] = nr, nc

        # 2-1. 만약 이동한 방향에 플레이어가 없다면
        if table[nr][nc] == 0:
           gun = change_gun(nr, nc, gun, player)
           table[nr][nc] = player  # 이거 빼먹음

        # 2-2-1. 만약 이동한 방향에 플레이어가 있는 경우
        else:
            fight(player, table[nr][nc], nr, nc)

print(*answer[1:])