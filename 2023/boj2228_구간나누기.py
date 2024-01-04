n, m = map(int, input().split())
con = [[0]+[-987654321]*m for _ in range(n+1)]
notcon = [[0]+[-987654321]*m for _ in range(n+1)]
nums = list(int(input()) for _ in range(n))
for i in range(1, n+1):
    for j in range(1, m):
        notcon[i][j] = max(con[i-1][j], notcon[i-1][j])
        con[i][j] = max(con[i-1][j], notcon[i-1][j-1])+nums[i-1]
        # print('========포함========')
        # print(*con, sep='\n')
        print(i, j)
        print(*con, sep='\n')
print(max(con[n][m], notcon[n][m]))
