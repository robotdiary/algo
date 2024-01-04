# 1:57 ~ 2:46
from collections import deque


def check_star(lst):
    cnt = 0
    lst = deque(lst)
    while len(lst) == 4:
        cnt += 1
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            cr, cc = lst.popleft()
            arr[cr][cc] = 1
            ni, nj = cr + di, cc + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != '.':
                lst.append((ni, nj))
    return cnt


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
stars = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != '.':
            # 별인지 확인
            star = []
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = i + dr, j + dc
                if not 0 <= nr < n or not 0 <= nc < m or arr[nr][nc] == '.':
                    break
                else:
                    star.append((nr, nc))
            else:
                arr[i][j] = 1
                stars += [i + 1, j + 1, check_star(star)]
for check in arr:
    if '*' in check:
        print(-1)
        break
else:
    print(len(stars) // 3)
    for p in range(0, len(stars), 3):
        print(*stars[p:p + 3])