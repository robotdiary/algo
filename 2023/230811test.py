from collections import deque
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    q = deque([(r, c)])
    visited = {(r, c)}
    arr[r][c] = 0
    day = 0
    while q:
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]:
                    arr[nr][nc] = 0
                    visited.add((nr, nc))
                    q.append((nr, nc))
        else:
            day += 1
    answer = 0
    for lst in arr:
        answer += lst.count(1)

    print(f'#{tc} {day} {answer}')