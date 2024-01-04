def comb(depth, start, lst):
    if depth == 3:
        bfs(lst, len(rooms) - 3, virus[:])
        return
    for room in range(start, len(rooms)):
        comb(depth + 1, room + 1, lst + [rooms[room]])


def bfs(lst, cnt, q):  # 벽이 된 lst
    global answer
    visited = [[0]*m for _ in range(n)]
    visited[q[-1][0]][q[-1][1]] = 1
    while q:
        cr, cc = q.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                if arr[nr][nc] != '1' and (nr, nc) not in lst:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    if arr[nr][nc] == '0':
                        cnt -= 1
                        if cnt <= answer:
                            return
    answer = cnt


n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]  # 문자열

rooms = []  # 35개 -> 32개
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            rooms.append((i, j))
        elif arr[i][j] == '2':
            virus.append((i, j))

answer = 0
comb(0, 0, [])
print(answer)