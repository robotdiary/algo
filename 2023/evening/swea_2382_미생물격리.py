'''
tuple에 할당하려고 함
'<' not supported between instances of 'dict' and 'int'
원래 있던 자리에 내가 흔적이 남는지 확인하고 남았다면 지워 / 덮어씌워졌으면 지우면 안 돼
answer 셀 때, 딕셔너리에서 죽은 미생물은 세면 안 돼
'''
di = (0, -1, 1, 0, 0)
dj = (0, 0, 0, -1, 1)
oppo = {1: 2, 2: 1, 3: 4, 4: 3}
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # arr = [[[] for _ in range(N)] for _ in range(N)]
    arr = [[0] * N for _ in range(N)]
    players = {}
    for idx in range(1, K + 1):
        R, C, S, D = map(int, input().split())  #
        players[idx] = [R, C, S, D, S]  # 좌표, 크기, 방향, 대표자
        arr[R][C] = idx
    # print(*arr, sep='\n')
    # print(players)
    # print()

    visited = [0] * (K + 1)
    for turn in range(M):
        for player in range(1, K + 1):
            if visited[player]:
                continue
            cr, cc, nums, d, boss = players[player]

            if arr[cr][cc] == player:
                arr[cr][cc] = 0  # 원래 있던 자리에서 지워야지

            nr, nc = cr + di[d], cc + dj[d]
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                nums //= 2
                d = oppo[d]
            if nums == 0:
                visited[player] = 1
                continue

            players[player] = [nr, nc, nums, d, nums]
            # print(tc)
            # print(arr[nr][nc])
            # print(player)
            if arr[nr][nc] and arr[nr][nc] < player:
                if players[arr[nr][nc]][-1] > players[player][-1]:
                    players[arr[nr][nc]][2] += players[player][2]
                    visited[player] = 1
                else:
                    players[player][2] += players[arr[nr][nc]][2]
                    visited[arr[nr][nc]] = 1
                    arr[nr][nc] = player

            else:
                arr[nr][nc] = player
        # print(tc)
        # print(*arr, sep='\n')
        # print(players)
    answer = 0
    for key, value in players.items():
        if visited[key] == 0:  # 죽은 미생물은 세지 마
            answer += value[2]
    print(f'#{tc} {answer}')