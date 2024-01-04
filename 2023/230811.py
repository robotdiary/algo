n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = 0
for i in range(n - 1, -1, -1):
    cnt = k // coins[i]
    answer += cnt
    k -= coins[i] * cnt
print(answer)