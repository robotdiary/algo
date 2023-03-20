# boj 2839 설탕 배달 (S4)
N = int(input())
dp = [10000]*5001
dp[3], dp[5] = 1, 1
for i in range(6, 5001):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)
if dp[N] >= 10000:
    print(-1)
else:
    print(dp[N])
