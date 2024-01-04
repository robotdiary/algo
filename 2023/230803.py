from collections import deque
for tc in range(1, int(input()) + 1):
    n = int(input())
    r, c = map(int, input().split())
    gr, gc = map(int, input().split())

    q = deque([(r, c)])
    visited = [[-1] * n for _ in range(n)]
    visited[r][c] = 0
    while q:
        cr, cc = q.popleft()
        if (cr, cc) == (gr, gc):
            break
        for dr, dc in (-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + 1

    print(visited[gr][gc])