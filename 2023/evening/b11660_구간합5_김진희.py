import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp1 = [[0] * (n + 1)] + [[0] * (n + 1) for _ in range(n)]
dp = [[0] * (n + 1)] + [[0] * (n + 1) for _ in range(n)]

# 이제 가로 누적합으로 dp를 채워준다
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp1[i][j] = dp1[i][j - 1] + arr[i - 1][j - 1]
        dp[i][j] = dp1[i][j] + dp[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] + dp[x1 - 1][y1 - 1] - dp[x2][y2 - (y2 - y1) - 1] - dp[x2 - (x2 - x1) - 1][y2])

