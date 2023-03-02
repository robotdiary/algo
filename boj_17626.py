# 네네무
n = int(input())
dp = [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2]  # 11
for _ in range(11, n+1):
    dp.append(min([dp[-1 * (i ** 2)] for i in range(1, int(len(dp) ** (1/2)) + 1)]) + 1)
print(dp[n])

# 제곱수 전의 수가 가진 최소값 + 제곱수(1)를 하는게 현재 가질 수 있는 최소가 될 거라는 가정