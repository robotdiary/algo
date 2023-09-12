'''
평범하게 상어를 잡는 작전
'''
from collections import deque


def move(x, y, distance, direction):
    for i in range(distance):
        nr, nc = x + di[direction], y + dj[direction]
        if 0 <= nr < n and 0 <= nc < m:
            x, y = nr, nc
        else:
            direction = turn[direction]
            nr, nc = x + di[direction], y + dj[direction]
            x, y = nr, nc
    return x, y, direction

n, m, k = map(int, input().split())
sharks = deque()
for _ in range(k):
    rr, cc, ss, dd, zz, = tuple(map(int, input().split()))
    sharks.append((rr - 1, cc - 1, ss, dd, zz))
answer = set()
di = (0, -1, 1, 0, 0)
dj = (0, 0, 0, 1, -1)
turn = {1: 2, 2: 1, 3: 4, 4: 3}

for man in range(m):
    visited = [[0] * m for _ in range(n)]
    catch = (100, 100, 0)
    # [1] 가까운 아래 상어 잡기
    for r, c, s, d, z in sharks:
        if c == man and r < catch[0]:
            catch = (r, c, z)
    answer.add(catch[2])

    # [2] 상어 이동
    for d in range(len(sharks)):
        r, c, s, d, z = sharks.popleft()
        if z in answer:
            continue
        r, c, d = move(r, c, s, d)
        if visited[r][c] == 0:
            visited[r][c] = (z, s, d)
        else:
            visited[r][c] = max(visited[r][c], (z, s, d))

    # [3] 상어 추가
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                sharks.append((i, j, visited[i][j][1], visited[i][j][2], visited[i][j][0]))
print(sum(answer))