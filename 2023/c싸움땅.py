'''
123ms	31MB    3시간
90분 : 총체적 난국
44분 : tc 6틀림
28분 : 재구현 → 틀림
18분 : 포기
끝나고 준호님 디버깅

[기억해야할 잘못]
내 방향을 info에서 미리 바꿔주지 않았는데,
뒤에서 d가 아닌 info[4]를 사용해서 벽에 부딪혔을 때, 올바른 방향으로 가지 못함
같은 nr, nc에 두 player가 겹치더라도 일단 내가 위치를 변경했으면 반영하고,
변경되는대로 바꿔주는 것이 훨씬 깔끔하고 편한 것 같다.

[소회]
이렇게 아예 모르겠는 경우는 처음이라 너무 답답했다.
세시간에 포기하고 뒤 문제를 풀었는데, 다시 풀었으면 됐을까? 아님 2시간째 미리 바꿨어야 했을까?
정답은 모르겠지만, 지금 생각해보면 linked lst를 어차피 2시간에 못 풀었을 것 같으니
뒤 문제가 시간 초과 문제일 걸 안다면 하나만 붙잡는 게 역시 나을 것 같다.

[아이디어]
총은 lst에 담는다 -> 총 lst를 돌면서 나와 더 큰 애를 교환하는 방식으로 총을 바꾼다 (0이 추가되는 단점)
dict{player : info} 사용
table 배열에 player를 올려둔다 -> 위치를 바꿨을 때, 다른 사람을 만나는지 확인 & 눈으로 디버깅 가능
winner와 loser 변수로 승패를 확인하고 각각 움직인다. -> player가 이겼는지 자리에 있던 자가 이겼는지 상관 X
'''


def change_gun(g, x, y):
    mx = g
    for ng in range(len(arr[x][y])):
        if arr[x][y][ng] > mx:
            arr[x][y][ng], mx = mx, arr[x][y][ng]
    return mx


def move_lose(idx, r, c):
    d = players[idx][2]
    for k in range(4):
        lr, lc = r + di[d % 4], c + dj[d % 4]
        if 0 <= lr < N and 0 <= lc < N and table[lr][lc] == 0:
            players[idx] = [lr, lc, d, players[idx][3], change_gun(0, lr, lc)]
            table[lr][lc] = idx
            return
        else:
            d += 1


N, M, K = map(int, input().split())
arr = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]  # 총을 리스트로 받기
table = [[0] * N for _ in range(N)]  # player의 위치
players = {}                         # {플레이어 번호 : 정보} 1번부터
for idx in range(1, M + 1):
    x, y, d, s = map(int, input().split())
    table[x-1][y-1] = idx
    players[idx] = [x-1, y-1, d, s, 0]  # 좌표, 방향, 힘, 총

di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)
oppo = {0: 2, 2: 0, 1: 3, 3: 1}
answer = [0] * (M + 1)
for tc in range(K):
    for player in range(1, M + 1):
        # [1] 이동
        cr, cc, direction, power, gun = players[player]
        table[cr][cc] = 0  # 일단 나와
        d = direction % 4
        nr, nc = cr + di[d], cc + dj[d]
        if not 0 <= nr < N or not 0 <= nc < N:
            d = oppo[d]
            nr, nc = cr + di[d], cc + dj[d]

        ## 중요 ! 플레이어의 변한 정보를 미리 저장해둬야 뒤에서 안 헷갈리게 사용할 수 있음 ! ##
        players[player] = nr, nc, d, power, gun

        # [2] 사람 없으면 위치랑 총만 바꾼다
        if table[nr][nc] == 0:
            players[player][4] = change_gun(gun, nr, nc)
            table[nr][nc] = player

        # [3] 사람 있으면 큰일
        else:
            enemy = table[nr][nc]
            enemy_info = players[enemy]  # x, y, d, s, g

            fight = power + gun - enemy_info[3] - enemy_info[4]
            if fight > 0 or (fight == 0 and power > enemy_info[3]):
                answer[player] += fight
                if enemy_info[4]:  # 진 놈 총 버려
                    arr[nr][nc].append(enemy_info[4])
                players[player][4] = change_gun(gun, nr, nc)
                table[nr][nc] = player
                move_lose(enemy, nr, nc)

            else:
                answer[enemy] += -fight
                if gun:
                    arr[nr][nc].append(gun)
                players[enemy][4] = change_gun(enemy_info[4], nr, nc)
                move_lose(player, nr, nc)

print(*answer[1:])
