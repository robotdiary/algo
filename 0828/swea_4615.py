# 4615 재미있는 오셀로 게임(D3) 12:30
def turn_w(r, c, color, non):
    global arr
    # arr[r][c] = color
# [1] 가로 돌 바꾸기
    cnt = arr[r].count(color)
    if cnt == 1 and arr[r].index(color) < c:
        arr[arr[r].index(color):c+1] = [color] * (c+1-arr[r].index(color))
    elif cnt == 1 and arr[r].index(color) > c:
        arr[c:arr[r].index(color) + 1] = [color] * (arr[r].index(color)+1-c)
    elif cnt > 1:
        for i in range(n):
            if arr[r][i]==



# [2] 세로 돌 바꾸기
def turn_h(r, c, color, non):
    global arr
    arr[r][c] = color
    for hr, hc in [(1, 0), (-1, 0)]:
        if r+hr < n and c+hc < n and arr[r+hr][c+hc] == non:
            turn_h(r+hr, c+hc, color, non)
        else:
            continue
    return


    # [3] 대각선 돌 바꾸기
def turn_s(r, c, color, non):
    global arr
    arr[r][c] = color
    for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nr = r+x
        nc = c+y
        if nr < n and nc < n and arr[nr][nc] == non:
            while nr+1 < n and nc+1 < n and arr[nr][nc] == non:
                nr += 1
                nc += 1
                arr[nr][nc] = color
    return


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split()) # 보드의 길이, 돌 놓는 횟수
    arr = [[0] * n for _ in range(n)]
    # [0] 기본 배치
    arr[n//2-1][n//2-1], arr[n//2][n//2] = 2, 2
    arr[n//2-1][n//2],arr[n//2][n//2-1] = 1, 1
    for i in range(m):
        stone = list(map(int, input().split()))
        if stone[2] == 1: # 흑돌 1
            turn_w(stone[1]-1, stone[0]-1, 1, 2)
            turn_h(stone[1]-1, stone[0]-1, 1, 2)
            turn_s(stone[1]-1, stone[0]-1, 1, 2)
        else: # 백돌 2
            turn_w(stone[1]-1, stone[0]-1, 2, 1)
            turn_h(stone[1]-1, stone[0]-1, 2, 1)
            turn_s(stone[1]-1, stone[0]-1, 2, 1)
    black = 0
    white = 0
    for i in range(n):
        black += arr[i].count(1)
        white += arr[i].count(2)
    print(f'{tc} {black} {white}')