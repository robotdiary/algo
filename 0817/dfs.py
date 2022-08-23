v, e = map(int, input().split())
# [1] 자료 구조화 하기 - 2차원 리스트로
arr = [[0] * (v + 1) for _ in range(v + 1)] # 인덱스랑 숫자 맞출려고 0은 비움
start_end = list(map(int, input().split())) # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
for i in range(e): # 간선 개수만큼 0, 1, 2, 3, 4, 5, 6, 7
    arr[start_end[2*i]][start_end[2*i+1]] = 1 # 0 1, 2 3, 4 5, 6 7, 8 9, 10 11, 12 13, 14 15
    arr[start_end[2*i+1]][start_end[2*i]] = 1
# [2] 스택
# stack = [1] # 시작은 1
# visited = []
# while stack:
#     current = stack.pop()
#     if current not in visited:
#         visited.append(current)
#     for destination in range(v + 1):
#         if arr[current][destination] and destination not in visited:
#             stack.append(destination)

# [3] 재귀
# def dfs(n):
#     if n not in visited:  # 우선 visited 없으면 넣어줌
#         visited.append(n)
#
#     for destination in range(v+1):
#         if arr[n][destination] and destination not in visited:
#             dfs(destination)  # 다음 재귀 깊이로 이동
# visited = []
# dfs(1)
print(*visited)

