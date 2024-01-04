from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
# 고슴도치, 물 위치찾기
sr, sc = -1, -1
waters = set()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            sr, sc = i, j
            arr[i][j] = '.'
        elif arr[i][j] == '*':
            waters.add((i, j))

q = deque([(sr, sc)])
visited = deque(list(waters))  # 여기서 pop하면서 스택을 쌓을건데 set으로 하면 어떡해@@@@!!!!!
day = 0
flag = 0
while q:
    for _ in range(len(visited)):
        water = visited.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = water[0] + dr, water[1] + dc
            if 0 <= nr < r and 0 <= nc < c and (nr, nc) not in waters and arr[nr][nc] == '.':
                visited.append((nr, nc))
                waters.add((nr, nc))

    for _ in range(len(q)):
        cr, cc = q.popleft()
        if arr[cr][cc] == 'D':
            print(day)
            flag = 1
            break

        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c and (nr, nc) not in waters:
                if arr[nr][nc] in {'.', 'D'}:
                    q.append((nr, nc))
                    waters.add((nr, nc))
    else:
        day += 1

    if flag:
        break
else:
    print("KAKTUS")