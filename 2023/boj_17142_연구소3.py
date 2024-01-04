from collections import deque


def bfs(lst):
    global answer
    visit = set(lst)
    hour = 1
    r = room
    while lst:
        if hour >= answer:
            return
        for h in range(len(lst)):
            cr, cc = lst.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    if arr[nr][nc] == '0':
                        visit.add((nr, nc))
                        lst.append((nr, nc))
                        r -= 1
                        if not r:
                            answer = min(answer, hour)
                    elif arr[nr][nc] == '2':
                        visit.add((nr, nc))
                        lst.append((nr, nc))
        hour += 1


def comb(depth, selected, idx):
    if depth == m:
        bfs(deque(selected))
        return

    for i in range(idx, cnt):
        if not visited[i]:
            visited[i] = 1
            comb(depth + 1, selected + [virus[i]], i + 1)
            visited[i] = 0


n, m = map(int, input().split())  # 4~50, 1~10
arr = [list(input().split()) for _ in range(n)]

virus = []
room = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '0':
            room += 1
        elif arr[i][j] == '2':
            virus.append((i, j))

cnt = len(virus)
answer = 9876554321
# 바이러스 중 m개 선택
if room:
    visited = [0] * len(virus)
    comb(0, [], 0)
else:
    answer = 0

if answer == 9876554321:
    print(-1)
else:
    print(answer)
