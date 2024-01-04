'''
조합에서 하나씩 고르는 거 먼저 확인
그리고 하나씩 늘려가며 고르기 ( 최소를 찾으면 멈추기 위하여 )
'''
def dfs(cnt, depth):
    global flag
    q = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    cnt -= 1
    while q:
        cr, cc = q.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == '.':
                    cnt -= 1
                    if not cnt:
                        flag = depth
                        return True
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    return False


def cur(depth, selected, start):
    if depth == len(selected):
        for r, c in selected:
            arr[r][c] = '.'
        dfs(rooms+depth, depth)
        for r, c in selected:
            arr[r][c] = '#'
        return

    for idx in range(start, len(walls)):
        if not check[idx]:
            check[idx] = 1
            cur(depth, selected + [walls[idx]], idx + 1)
            if flag:
                return
            check[idx] = 0


N = int(input())
arr = [list(input()) for _ in range(N)]

rooms = 0
sr, sc = 0, 0
walls = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            walls.append((i, j))
        else:
            rooms += 1
            sr, sc = i, j

check = [0] * len(walls)

flag = 0
if rooms < 2 or dfs(rooms, 0):
    print(0)
else:
    for i in range(1, 7):
        cur(i, [], 0)
        if flag:
            print(flag)
            break
    else:
        print(-1)
