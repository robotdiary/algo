from collections import deque

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q = deque()  # 좌표, 시간, 현재
    visited = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                q.append((arr[i][j], arr[i][j], i, j))
                visited.add((i, j))

    answer = 0
    while q and answer < K:
        grow = []  # 크기, 현재, 좌표
        for day in range(len(q)):
            time, current, cr, cc = q.popleft()
            current -= 1
            if current == -1:
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if (nr, nc) not in visited:
                        grow.append((time, nr, nc))
            if current > -time:
                q.append((time, current, cr, cc))

        grow.sort(reverse=True)
        for t, x, y in grow:
            if (x, y) not in visited:
                visited.add((x, y))
                q.append((t, t, x, y))
        answer += 1

    print(f'#{tc} {len(q)}')

