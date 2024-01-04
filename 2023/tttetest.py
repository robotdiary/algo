from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # [1] 현위치와 마그마 위치 찾기
    r, c = -9, -9
    magma = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 3:
                magma.add((i, j))
            elif arr[i][j] == 4:
                r, c = i, j
                arr[i][j] = 1
    if (r, c) == (-9, -9):
        print(f'#{tc} -1')
        continue
    # [2] 갈 수 있는 곳 bfs로 방문, 날짜 0부터
    day = 0
    q = deque([(r, c)])
    visited = set()    # 마그마 퍼진 곳
    before = {(r, c)}  # 밟았던 데
    while q:
        # [3] 마그마 위치 돌면서 마그마 추가
        for magma_r, magma_c in magma:
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr = magma_r + dr
                nc = magma_c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    if arr[nr][nc] == 1:
                        visited.add((nr, nc))
        magma |= visited

        # [4] 내 위치에서 갈 수 있는 곳 찾기
        for _ in range(len(q)):
            cr, cc = q.popleft()

            # [5] 대피소면 다행
            if arr[cr][cc] == 2:
                visited = -1
                break

            # if (cr, cc) not in magma:
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in magma:
                    if arr[nr][nc] in {1, 2} and (nr, nc) not in before:
                        q.append((nr, nc))
                        before.add((nr, nc))

        else:
            day += 1

        if visited == -1:
            break
    else:
        day = -1

    print(f'#{tc} {day}')