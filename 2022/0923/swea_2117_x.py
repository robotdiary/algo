# 2117. [모의 SW 역량테스트] 홈 방범 서비스
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    houses = set()
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                houses.add((i, j))
    k = n
    if n % 2 == 0:
        k = n + 1
    for i in range(n):
        for j in range(n):
            ans = 0
            Q = deque([(3, 3)])
            visited = []
            depth = 0
            while Q:
                if depth >= k:
                    for house in visited:
                        if house in houses:
                            ans += 1
                    if ans * m >= k * k + (k - 1) * (k - 1):
                        ans = max(ans, answer)
                    ans = 0
                    Q = deque([(3, 3)])
                    visited = []
                    depth = 0
                    k -= 1
                    continue
                for q in range(len(Q)):
                    nr, nc = Q.popleft()
                    if (nr, nc) not in visited:
                        visited.append((nr, nc))
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= nr + dr < n and 0 <= nc + dc < n and (nr + dr, nc + dc) not in visited:
                            Q.append((nr + dr, nc + dc))
                depth += 1

    print(f'#{tc} {answer}')