# 체스판 다시 칠하기
def wb_board(x, y):
    cnt = 0
    for ii in range(0, 7, 2):
        for jj in range(0, 8, 2):
            if arr[x + ii][y + jj] != 'W':
                cnt += 1
            if arr[x + ii][y + jj + 1] != 'B':
                cnt += 1
    for r in range(1, 8, 2):
        for c in range(0, 8, 2):
            if arr[x + r][y + c] != 'B':
                cnt += 1
            if arr[x + r][y + c + 1] != 'W':
                cnt += 1
    return min(answer, cnt)


def bw_board(x, y):
    cnt = 0
    for ii in range(0, 7, 2):
        for jj in range(0, 8, 2):
            if arr[x + ii][y + jj] != 'B':
                cnt += 1
            if arr[x + ii][y + jj + 1] != 'W':
                cnt += 1
    for r in range(1, 8, 2):
        for c in range(0, 8, 2):
            if arr[x + r][y + c] != 'W':
                cnt += 1
            if arr[x + r][y + c + 1] != 'B':
                cnt += 1
    return min(answer, cnt)


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

answer = 98765
for i in range(n - 7):
    for j in range(m - 7):
        answer = wb_board(i, j)
        answer = bw_board(i, j)

print(answer)