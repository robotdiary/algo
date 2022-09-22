# 1861. 정사각형 방 D4
# [2]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    answer = (-1, -1)
    for i in range(n):
        for j in range(n):
            cnt = 1
            nr, nc = i, j
            while True:
                for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if arr[nr+d[0]][nc+d[1]] == arr[nr][nc] + 1:
                        nr = nr+d[0]
                        nc = nc+d[1]
                        cnt += 1
                        break
                else:
                    break
            if cnt > count:
                count = cnt
            elif cnt == count:
                answer = (i, j)
    print(f'#{tc} {arr[answer[0]][answer[1]]} {cnt}')


# [1] dfs 시간초과
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 0
#     answer = (-1, -1)
#     for i in range(n):
#         for j in range(n):
#             stack = [(i, j)]
#             visited = []
#             while stack:
#                 nr, nc = stack.pop()
#                 if (nr, nc) not in visited:
#                     visited.append((nr, nc))
#                 for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     if 0 <= nr+d[0] < n and 0 <= nc + d[1] < n and (nr+d[0], nc+d[1]) not in visited:
#                         if arr[nr][nc] + 1 == arr[nr+d[0]][nc+d[1]]:
#                             stack.append((nr+d[0], nc+d[1]))
#             # print(visited)
#             if len(visited) > cnt:
#                 cnt = len(visited)
#                 answer = (i, j)
#             elif len(visited) == cnt:
#                 if arr[answer[0]][answer[1]] > arr[i][j]:
#                     answer = (i, j)
#     print(f'#{tc} {arr[answer[0]][answer[1]]} {cnt}')
