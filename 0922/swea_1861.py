# 1861. 정사각형 방 D4
# [2] 시간초과 해결
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    answer = (-1, -1)
    # [1] 모든 좌표에 대하여 탐색
    for i in range(n):
        for j in range(n):
            # 최대 count만큼 갈 수 없는 큰 수는 제외
            if arr[i][j] > n ** 2 - count:
                continue
            # [2] 여기부터 arr[i][j]의 사방탐색 & dfs
            cnt = 1
            nr, nc = i, j
            visited = set()
            while True:
                # 백트래킹 필수
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= nr + d[0] < n and 0 <= nc + d[1] < n and (nr + d[0], nc + d[1]) not in visited:
                        # 1 큰 수일때만, stack에 추가
                        if arr[nr+d[0]][nc+d[1]] == arr[nr][nc] + 1:
                            nr = nr+d[0]
                            nc = nc+d[1]
                            cnt += 1
                            break # 같은 수는 없으므로 break
                else: # 네 군데 중 갈 곳을 못 찾으면 와일문 자체를 빠져나감
                    break
            # 더 큰 수면 바로 바꾸지만,
            if cnt > count:
                count = cnt
                answer = (i, j)
            # 같은 수면 더 작은 숫자를 가진 것으로 출력해야 함
            elif cnt == count and arr[i][j] < arr[answer[0]][answer[1]]:
                answer = (i, j)
    print(f'#{tc} {arr[answer[0]][answer[1]]} {count}')

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
