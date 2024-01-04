# 미로 탐색
import sys
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

q = deque()
q.append((0, 0))
visited = set()
visited.add((0, 0))
answer = 0
while q:
    answer += 1
    for bfs in range(len(q)):
        nr, nc = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= nr+dr < n and 0 <= nc + dc < m:
                if arr[nr + dr][nc + dc] and (nr + dr, nc + dc) not in visited:
                    if (nr + dr, nc + dc) == (n-1, m-1):
                        print(answer+1)
                        sys.exit()
                    q.append((nr + dr, nc + dc))
                    visited.add((nr + dr, nc + dc))
