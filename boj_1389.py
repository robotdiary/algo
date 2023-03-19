# 케빈 베이컨의 6단계 법칙
n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

bacon = [0] * (n + 1)

print(arr)