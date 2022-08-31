# 5105 미로의 거리 (D3)
# bfs를 재귀로
def maze_distance(depth, stk):
    global answer
    nr, nc = stk
    if (nr, nc) not in set(visited):
        visited.append((nr, nc))
    for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if answer:
            return
        if 0 <= (nr + dr) < n and 0 <= (nc + dc) < n and (nr + dr, nc + dc) not in visited:
            if maze[nr + dr][nc + dc] == 0:
                maze_distance(depth + 1, (nr + dr, nc + dc))
            elif maze[nr + dr][nc + dc] == 2:
                answer = depth
                return


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    r, c = 0, 0
    for i in range(n):
        if 3 in maze[i]:
            r, c = i, maze[i].index(3)
            break
    stack = (r, c)
    visited = []
    answer = 0

    # 함수 콜
    maze_distance(0, stack)
    print(f'#{tc} {answer}')


# Dfs는 시간초과
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(n)]
#     r, c = 0, 0
#     for i in range(n):
#         if 3 in maze[i]:
#             r, c = i, maze[i].index(3)
#     stack = [(r, c)]
#     visited = []
#     result = 0
#     while stack:
#         nr, nc = stack.pop()
#         if (nr, nc) not in set(visited):
#             visited.append((nr, nc))
#         cnt = 0
#         for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
#             if 0 <= (nr + dr) < n and 0 <= (nc + dc) < n and (nr + dr, nc + dc) not in visited:
#                 if maze[nr + dr][nc + dc] == 0:
#                     stack.append((nr + dr, nc + dc))
#                     cnt += 1
#                 elif maze[nr + dr][nc + dc] == 2:
#                     result = (len(visited) - 1)
#                     break
#         if cnt == 0:
#             visited = [(r, c)]
#         else:
#             cnt == 0
#     print(f'#{tc} {result}')

