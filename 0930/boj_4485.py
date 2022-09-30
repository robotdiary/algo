# [4] 다익스트라에 visited를 추가 (시간 280ms, 메모리 34444kb, 길이 787b)
# from heapq import heappop, heappush
#
# n = int(input())
# tc = 0
# while n:
#     tc += 1
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     adj = [[987654321] * n for _ in range(n)]
#     adj[0][0] = arr[0][0]
#
#     q = [(adj[0][0], 0, 0)]
#     visited = set()
#     while q:
#         w, nr, nc = heappop(q)
#         if (nr, nc) not in visited:
#             adj[nr][nc] = w
#             visited.add((nr, nc))
#
#             for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 if 0 <= nr+dr < n and 0 <= nc + dc < n and (nr+dr, nc+dc) not in visited:
#                     if adj[nr][nc] + arr[nr+dr][nc+dc] < adj[nr+dr][nc+dc]:
#                         heappush(q, (adj[nr][nc] + arr[nr+dr][nc+dc], nr+dr, nc+dc))
#
#     print(f'Problem {tc}: {adj[n-1][n-1]}')
#     n = int(input())

# [3] 다익스트라로  (시간 252ms, 메모리 32908kb, 길이 674b)
from heapq import heappop, heappush
n = int(input())
tc = 0
while n:
    tc += 1
    arr = [list(map(int, input().split())) for _ in range(n)]
    adj = [[987654321] * n for _ in range(n)]
    adj[0][0] = arr[0][0]

    q = [(adj[0][0], 0, 0)]
    while q:
        w, nr, nc = heappop(q)
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= nr+dr < n and 0 <= nc + dc < n:
                if adj[nr][nc] + arr[nr+dr][nc+dc] < adj[nr+dr][nc+dc]:
                    adj[nr+dr][nc+dc] = adj[nr][nc] + arr[nr+dr][nc+dc]
                    heappush(q, (adj[nr+dr][nc+dc], nr+dr, nc+dc))

    print(f'Problem {tc}: {adj[n-1][n-1]}')
    n = int(input())

# [2] bfs 누적합을 가지고 다니는게 아니라, adj배열에서 가져다 씀
# from collections import deque
# n = int(input())
# tc = 0
# while n:
#     tc += 1
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     adj = [[987654321] * n for _ in range(n)]
#     adj[0][0] = arr[0][0]
#     # bfs
#     q = deque([(0, 0)])
#     visited = set()
#     while q:
#         nr, nc = q.popleft()
#         for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             if 0 <= nr+dr < n and 0 <= nc + dc < n and adj[nr][nc] + arr[nr+dr][nc+dc] < adj[nr+dr][nc+dc]:
#                 adj[nr+dr][nc+dc] = adj[nr][nc] + arr[nr+dr][nc+dc]
#                 q.append((nr+dr, nc+dc))
#
#     print(f'Problem {tc}: {adj[n-1][n-1]}')
#     n = int(input())

# [1] bfs 맞았지만 시간 초과, pypy readline으로 통과
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# tc = 0
# while n:
#     tc += 1
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     adj = [[987654321] * n for _ in range(n)]
#     # bfs
#     q = deque([(0, 0, arr[0][0])])
#     visited = set()
#     while q:
#         nr, nc, w = q.popleft()
#         for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             if 0 <= nr+dr < n and 0 <= nc + dc < n and w + arr[nr+dr][nc+dc] < adj[nr+dr][nc+dc]:
#                 adj[nr+dr][nc+dc] = w + arr[nr+dr][nc+dc]
#                 q.append((nr+dr, nc+dc, w + arr[nr+dr][nc+dc]))
#
#     print(f'Problem {tc}: {adj[n-1][n-1]}')
#     n = int(input())