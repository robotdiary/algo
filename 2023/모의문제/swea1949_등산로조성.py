from collections import deque

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    peak = []
    # [0] 가장 높은 봉우리 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] > mx:
                mx = arr[i][j]
                peak = [(i, j)]
            elif arr[i][j] == mx:
                peak.append((i, j))

    answer = 0
    q = deque()
    for pr, pc in peak:
        q.append((mx, [(pr, pc)], 0))
    while q:
        # for day in range(len(q)):
        height, visited, flag = q.popleft()
        cr, cc = visited[-1][0], visited[-1][1]
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                if arr[nr][nc] < height:
                    q.append((arr[nr][nc], visited + [(nr, nc)], flag))
                elif not flag and arr[nr][nc] - K <= height - 1:
                    q.append((height - 1, visited + [(nr, nc)], 1))
                else:
                    answer = max(answer, len(visited))
                    # print(visited)

    print(f'#{tc} {answer}')
