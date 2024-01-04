# 에어컨
from collections import defaultdict
for tc in range(1, int(input()) + 1):
    n, m, k, t = map(int, input().split())
    status = defaultdict(set)
    for _ in range(k):
        filter_type, si, sj, h, w = map(int, input().split())
        for i in range(h):
            for j in range(w):
                if 0 <= si + i < n and 0 <= sj + j < m:
                    status[filter_type].add((si + i, sj + j))
    cool_set = status[0]
    for i in range(1, t + 1):
        if len(cool_set) == 0:
            break
        cool_set &= status[i]

    print(f'#{tc} {n * m - len(cool_set)}')

# 백두산4
# from collections import deque
#
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     l = 0  # 가장 긴 길이
#     answer = [] # 좌표
#     for i in range(n):
#         if l > 4546:
#             break
#         for j in range(m):
#             if arr[i][j]:
#                 q = deque([(i, j, 0)])
#                 visited = {i, j}
#                 depth = 0
#                 while q:
#                     for _ in range(len(q)):
#                         cr, cc, depth = q.popleft()
#                         if depth > l:
#                             l = depth
#                             answer = [(i + 1, j + 1), (cr + 1, cc + 1)]
#
#                         for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
#                             nr, nc = cr + dr, cc + dc
#                             if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and (nr, nc) not in visited:
#                                 q.append((nr, nc, depth + 1))
#                                 visited.add((nr, nc))
#                     depth += 1
#
#     if sum(answer[0]) < sum(answer[1]):
#         print(f'#{tc}', *answer[0])
#     elif sum(answer[0]) > sum(answer[1]):
#         print(f'#{tc}', *answer[1])
#     else:
#         if answer[0][0] < answer[1][0]:
#             print(f'#{tc}', *answer[0])
#         else:
#             print(f'#{tc}', *answer[1])