'''
h, v로 나눠서 주사위 굴리는 새로운 방법
원래 방법은 헷갈려서 계속 틀린다 (속도는 조금 더 빠른 듯 96 < 159)
'''
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [0] 점수판 미리 만들기
scores = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if scores[i][j] == 0:
            stack = [(i, j)]
            idx = 0
            scores[i][j] = 1
            while idx < len(stack):
                cr, cc = stack[idx]
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and scores[nr][nc] == 0:
                        if arr[nr][nc] == arr[i][j]:
                            stack.append((nr, nc))
                            scores[nr][nc] = 1
                idx += 1

            sm = arr[i][j] * len(stack)
            for r, c in stack:
                scores[r][c] = sm

h = [6, 2, 1, 5]  # 아래 앞 위 뒤
v = [6, 4, 1, 3]  # 아래 좌 위 우
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)  # 우 하 좌 상

cr, cc = 0, 0
d = 0
answer = 0
for tc in range(M):
    nr, nc = cr + di[d], cc + dj[d]
    if not 0 <= nr < N or not 0 <= nc < N:
        d = (d + 2) % 4
        nr, nc = cr + di[d], cc + dj[d]
    answer += scores[nr][nc]

    if d == 0:
        v = [v.pop()] + v
        h[0], h[2] = v[0], v[2]
    elif d == 1:
        h = h + [h.pop(0)]
        v[0], v[2] = h[0], h[2]
    elif d == 2:
        v = v + [v.pop(0)]
        h[0], h[2] = v[0], v[2]
    else:
        h = [h.pop()] + h
        v[0], v[2] = h[0], h[2]

    if h[0] > arr[nr][nc]:
        d = (d + 1) % 4
    elif h[0] < arr[nr][nc]:
        d = (d - 1) % 4

    cr, cc = nr, nc

print(answer)