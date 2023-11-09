'''
빨강이 먼저 빠져도 둘 다 빠지면 안 된다
빨간공이 제자리일 수 있지 둘 다 같은 위치인 걸 visited삼자
'''
from collections import deque


def move(nr, nc, dr, dc):
    dist = 0
    flag = 0
    while 0 <= nr + dr < N and 0 <= nc + dc < M and arr[nr + dr][nc + dc] != '#':
        nr += dr
        nc += dc
        dist += 1
        # 구멍이면 알려주자
        if arr[nr][nc] == 'O':
            flag = 1
            break
    return nr, nc, dist, flag


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
state = {}
# 위치 찾기 (벽 제외)
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if arr[i][j] == 'B':
            state['B'] = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            state['R'] = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            state['O'] = (i, j)

# q에 시작점 넣기
q = deque([(*state['R'], *state['B'])])
visited = {(*state['R'], *state['B'])}

# bfs
day = 1
Flag = 0
while q and day <= 10:
    for time in range(len(q)):
        a, b, c, d = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            redr, redc, redcnt, redflag = move(a, b, dr, dc)
            bluer, bluec, bluecnt, blueflag = move(c, d, dr, dc)
            # 제자리면? 방문한 곳이면? 둘 다 빠지면?
            if redflag and blueflag:
                continue
            # 같은 위치는 안 돼
            if redr == bluer and redc == bluec:
                if redcnt > bluecnt:
                    redr -= dr
                    redc -= dc
                else:
                    bluer -= dr
                    bluec -= dc

            # 구멍이면 탈출
            if (redr, redc) == state['O']:
                print(day)
                Flag = 1
                break
            if (bluer, bluec) == state['O']:
                continue
            if (redr, redc, bluer, bluec) not in visited:
                q.append((redr, redc, bluer, bluec))
                visited.add(((redr, redc, bluer, bluec)))
        if Flag:
            break

    else:
        day += 1

    if Flag:
        break
else:
    print(-1)
