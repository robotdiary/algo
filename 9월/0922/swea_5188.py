# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3
# [2] dp로 풀기
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        arr[0][i] = arr[0][i] + arr[0][i-1]
        arr[i][0] = arr[i][0] + arr[i-1][0]
    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] += min(arr[i-1][j], arr[i][j-1])
    print(f'#{tc} {arr[n-1][n-1]}')

# [1] dfs로 풀기
# def dfs(r, c, acc): # 누적합과 함께 다녀라
#     global answer
#
#     # 최소를 구하는 거니까 최대합이 이미 크면 그만두도록 백트래킹
#     if acc > answer:
#         return
#
#     # 끝까지 왔다면, 누적합 뱉어
#     if (r, c) == (n-1, n-1):
#         if answer > acc:
#             answer = acc
#         return
#
#     # dfs 본체
#     if (r, c) not in visited:
#         visited.append((r, c))
#
#     for d in [(0, 1), (1, 0)]:
#         if r + d[0] < n and c + d[1] < n:
#             dfs(r + d[0], c + d[1], acc + arr[r+d[0]][c+d[1]])
#
#
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     sr, sc = (0, 0)
#     visited = []
#     answer = 100
#     dfs(sr, sc, arr[0][0])
#     print(f'#{tc} {answer}')
