n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]
for i in range(n):
    dp.append(dp[i] + nums[i])
for tc in range(m):
    first, second = map(int, input().split())
    print(dp[second] - dp[first-1])