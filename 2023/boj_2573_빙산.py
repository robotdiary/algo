from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ice = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            ice.append((i, j, arr[i][j]))

answer = 0
flag = 1
while flag and len(ice) > 1:
    # print(ice)
    cnt = len(ice)
    q = deque([(ice[0])])
    visited = {(ice[0][0], ice[0][1])}
    changed = []
    while q:
        # print(q)
        cr, cc, height = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                if arr[nr][nc] == 0:
                    height -= 1
                else:
                    q.append((nr, nc, arr[nr][nc]))
                    visited.add((nr, nc))
        changed.append((cr, cc, height))
    if len(visited) == cnt:
        answer += 1
        ice = []
    else:
        flag = 0
        print(answer)
        break
    if flag:
        for rr, cc, hh in changed:
            arr[rr][cc] = 0 if hh < 1 else hh
            if hh > 0:
                ice.append((rr, cc, hh))
else:
    print(0)
