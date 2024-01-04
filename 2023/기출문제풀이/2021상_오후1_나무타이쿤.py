N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 나무
players = [tuple(map(int, input().split())) for _ in range(M)]  # 방향, 칸
table = [[0] * N for _ in range(N)]  # 약
table[-1][0], table[-1][1], table[-2][0], table[-2][1] = 1, 1, 1, 1

di = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dj = (0, 1, 1, 0, -1, -1, -1, 0, 1)
# print(players)
for turn in range(M):
    # [1] 특수 영양제를 이동 규칙에 따라 이동시킵니다.
    eatten = set()
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                table[i][j] = 0
                nr, nc = i + (di[players[turn][0]]*players[turn][1]), j + (dj[players[turn][0]]*players[turn][1])
                nr %= N
                nc %= N

                # [2] 영양제를 투입
                arr[nr][nc] += 1
                eatten.add((nr, nc))

    # [3] 대각선으로 성장
    for nr, nc in eatten:
        for dr, dc in (1, 1), (-1, -1), (-1, 1), (1, -1):
            if 0 <= nr+dr < N and 0 <= nc+dc < N and arr[nr+dr][nc+dc]:
                arr[nr][nc] += 1
    # print(eatten)
    # print('성장')
    # print(*arr, sep='\n')

    # [4] 특수 영양제 제외 / 높2 이상 높이- 2 / 해당 위치에 특수 영양제
    for i in range(N):
        for j in range(N):
            if (i, j) not in eatten and arr[i][j] > 1:
                arr[i][j] -= 2
                table[i][j] = 1
    # print('잘라')
    # print(*arr, sep='\n')
    # print('영양제')
    # print(*table, sep='\n')
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            answer += arr[i][j]
print(answer)