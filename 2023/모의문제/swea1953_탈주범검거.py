from collections import deque

turn = {1: [0, 1, 2, 3], 2: [0, 2], 3: [1, 3], 4: [0, 1], 5: [1, 2], 6: [2, 3], 7: [0, 3]}
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)  # 상 우 하 좌

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 1
    time = 1
    q = deque([(R, C)])
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    while q and time < L:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for d in turn[arr[cr][cc]]:
                nr, nc = cr + di[d], cc + dj[d]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    if arr[nr][nc] and (d + 2) % 4 in turn[arr[nr][nc]]:
                        q.append((nr, nc))
                        answer += 1
                        visited[nr][nc] = 1
        else:
            time += 1
    # print(*visited, sep='\n')
    print(f'#{tc} {answer}')