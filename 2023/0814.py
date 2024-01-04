def fibo(x):
    if dp[x]:
        return dp[x]
    dp[x] = min(fibo(x // 3), fibo(x // 2), fibo(x - 1)) + 1


n = int(input())
dp = [0] * (n + 3)
dp[1] = 1
dp[2] = 1
dp[3] = 1
fibo(n)
print(dp[n])