# from collections import deque
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = 0
#
# stack = []  # 섬을 찾을 dfs용 stack
# edges = []  # 섬의 가장자리
# # [1] 첫번째 섬 찾기
# for i in range(n):
#     if 1 in arr[i]:
#         stack.append((i, arr[i].index(1)))
#         arr[i][arr[i].index(1)] = 2
#         break
#
# # [2] 섬을 도는 dfs
# while stack:
#     while stack:
#         cr, cc = stack.pop()
#         for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
#             nr, nc = cr + dr, cc + dc
#             if 0 <= nr < n and 0 <= nc < m:
#                 if arr[nr][nc] == 1:
#                     arr[nr][nc] = 2
#                     stack.append((nr, nc))
#                 elif arr[nr][nc] == 0:
#                     edges.append((cr, cc, 0, dr, dc))  # 중복으로 들어감 좌표, 다리길이, 진행방향
#
#     # [3] 가장자리로부터 가장 가까운 다른 섬 찾기
#     q = deque(edges)
#     while q:
#         # for day in range(len(q)):
#         cr, cc, acc, dr, dc = q.popleft()
#         nr, nc = cr + dr, cc + dc
#         if 0 <= nr < n and 0 <= nc < m:
#             if arr[nr][nc] == 0:
#                 q.append((nr, nc, acc + 1, dr, dc))
#             # 다른 섬을 만났어
#             elif arr[nr][nc] == 1 and acc >= 2:
#                 answer += acc
#                 stack.append((nr, nc))
#                 arr[nr][nc] = 2  # 안 바꿔주고 1이면 무한루프를 돌게 된다.
#                 break
#
# # 불가능하면 -1
# for i in range(n):
#     if 1 in arr[i]:
#         answer = -1
#         break
# print(answer)


import heapq
from collections import deque


def dfs(stack):
    while stack:
        cr, cc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = island
                stack.append((nr, nc))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

island = 2
# 섬에 이름 짓기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = island
            dfs([(i, j)])
            island += 1

edges = [[99999] * (island + 1) for _ in range(island + 1)]
# 섬마다 연결선 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = i + dr, j + dc
                cnt = 0
                while 0 <= nr < n and 0 <= nc < m:
                    if arr[nr][nc] == arr[i][j]:
                        break
                    elif arr[nr][nc] == 0:
                        nr += dr
                        nc += dc
                        cnt += 1
                    else:
                        if cnt >= 2:
                            if cnt < edges[arr[i][j]][arr[nr][nc]]:
                                edges[arr[i][j]][arr[nr][nc]] = cnt
                        break

answer = 0
connected = 3
visited = [0] * island
stack = [2]
while stack:
    for

else:
    print(-1)