from collections import deque


def comb(start, depth, lst):
    global answer

    if depth == M:
        acc = 0
        for mr, mc in mans:
            acc += taxi(lst, mr, mc)
            if acc >= answer:
                return
        answer = acc
        return

    for idx in range(start, len(hosp)):
        if visited[idx] == 0:
            visited[idx] = 1
            comb(idx + 1, depth + 1, lst + [hosp[idx]])
            visited[idx] = 0


def taxi(lst, cr, cc):
    dist = 99999999
    for r, c in lst:
        d = abs(cr - r) + abs(cc - c)
        dist = min(dist, d)
    return dist


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# [0] 병원, 사람 찾기
hosp = []
mans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            mans.append((i, j))
        elif arr[i][j] == 2:
            hosp.append((i, j))

# 병원 고르기
visited = [0] * len(hosp)
answer = 99999999
comb(0, 0, [])

print(answer)