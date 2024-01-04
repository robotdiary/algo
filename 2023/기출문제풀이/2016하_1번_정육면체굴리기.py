'''
백준 - 주사위 굴리기
10월 2일 오전 10시 16분 - 10시 33분 (구현 15분)
'''
N, M, cr, cc, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = list(map(int, input().split()))

dice = [0] * 6  # 바닥, 천장, 좌, 앞, 우, 뒤
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

for tc in range(K):
    d = turn[tc]
    nr, nc = cr + di[d], cc + dj[d]
    if 0 <= nr < N and 0 <= nc < M:
        if d == 1:
            dice = [dice[4], dice[2], dice[0], dice[3], dice[1], dice[5]]
        elif d == 2:
            dice = [dice[2], dice[4], dice[1], dice[3], dice[0], dice[5]]
        elif d == 3:
            dice = [dice[5], dice[3], dice[2], dice[0], dice[4], dice[1]]
        else:
            dice = [dice[3], dice[5], dice[2], dice[1], dice[4], dice[0]]
        cr, cc = nr, nc

        # [1] 칸에 쓰여져 있는 수가 0이면 주사위의 바닥면에 쓰여져있는 수가 칸에 복사됩니다.
        if arr[cr][cc] == 0:
            arr[cr][cc] = dice[0]
        # 칸에 쓰여져 있는 수가 0이 아니면 칸에 쓰여져있는 수가 정육면체 바닥면으로 복사되며, 해당 칸의 수는 0이 됩니다.
        else:
            dice[0] = arr[cr][cc]
            arr[cr][cc] = 0

        print(dice[1])