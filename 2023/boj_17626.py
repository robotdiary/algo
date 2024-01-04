# 네네무
n = int(input())  # 수
first_root = int(n ** (1/2) // 1)  # 제일 큰 제곱근
ans = [0, 0, 0, 0, 0]
while first_root:
    parent = n - (first_root ** 2)
    answer = [first_root]
    while parent:
        if len(answer) >= len(ans):
            break
        next_root = int(parent ** (1/2) // 1)
        parent -= (next_root ** 2)
        answer.append(next_root)
    if len(answer) < len(ans):
        ans = answer
    first_root -= 1
print(len(ans))
# =======
# n = int(input())
# dp = [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2]  # 11
# for _ in range(11, n+1):
#     dp.append(min([dp[-1 * (i ** 2)] for i in range(1, int(len(dp) ** (1/2)) + 1)]) + 1)
# print(dp[n])
#
# # 제곱수 전의 수가 가진 최소값 + 제곱수(1)를 하는게 현재 가질 수 있는 최소가 될 거라는 가정
# >>>>>>> 1e23d4e7e00b53a8a857e325f760c1d5f26e3c83
