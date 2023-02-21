# 유기농 배추
T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 수
    arr = [[0]*m for _ in range(n)]
    print(arr)
    for cabbage in range(k):
        r, c = map(int, input().split())
        arr[r][c] = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                stack = [(i, j)]
                while stack:
                    cr, cc = stack.pop()
                    for nr, nc in [()]