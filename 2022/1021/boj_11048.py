# 백준 11048 이동하기 (S2)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# [1] 맨 윗줄은 옆에서만, 맨 앞줄은 위에서만 올 수 있다.
for i in range(1, m):
    arr[0][i] = arr[0][i] + arr[0][i-1]
for i in range(1, n):
    arr[i][0] = arr[i][0] + arr[i-1][0]
    
# [2] 세 방향중 가장 큰 쪽에서 오는 걸로 갱신
for i in range(1, n):
    for j in range(1, m):
        arr[i][j] = arr[i][j] + max(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
print(arr[-1][-1])