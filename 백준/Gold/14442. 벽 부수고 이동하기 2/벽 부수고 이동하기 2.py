from collections import deque
n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]
q = deque([(0, 0, 1, 0)])
visited = [[987654321] * m for _ in range(n)]
while q:
    cr, cc, acc, hit = q.popleft()
    if (cr, cc) == (n - 1, m - 1):
        print(acc)
        break
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == '1':
                if visited[nr][nc] > hit + 1 and hit + 1 <= k:
                    q.append((nr, nc, acc + 1, hit + 1))
                    visited[nr][nc] = hit + 1
            else:
                if visited[nr][nc] > hit:
                    q.append((nr, nc, acc + 1, hit))
                    visited[nr][nc] = hit
else:
    print(-1)