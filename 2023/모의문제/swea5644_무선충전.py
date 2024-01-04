from collections import deque


def bfs(x, y, c, p):  # 좌표, 범위, 크기
    q = deque([(x, y)])
    visited = [[0] * 10 for _ in range(10)]
    visited[x][y] = 1
    arr[x][y].add(p)
    time = 0
    while q and time < c:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    arr[nr][nc].add(p)
        else:
            time += 1


def find_mx(st):
    mx = 0
    target = 0
    for m in st:
        if powers[m] > mx:
            mx = powers[m]
            target = m
    return mx, target


di = (0, -1, 0, 1, 0)
dj = (0, 0, 1, 0, -1)  # 무, 상, 우, 하, 좌

for tc in range(1, int(input())+1):
    M, BC = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    arr = [[set() for _ in range(10)] for _ in range(10)]
    powers = {}
    for idx in range(1, BC + 1):
        X, Y, C, P = map(int, input().split())
        powers[idx] = P
        bfs(Y-1, X-1, C, idx)

    ar, ac = 0, 0
    br, bc = 9, 9
    answer = 0
    result = [0, 0]
    for turn in range(M + 1):
        ar += di[A[turn]]
        ac += dj[A[turn]]
        br += di[B[turn]]
        bc += dj[B[turn]]

        if arr[ar][ac] & arr[br][bc]:
            v, t = find_mx(arr[ar][ac] | arr[br][bc])
            if t in arr[ar][ac] & arr[br][bc]:
                answer += v + find_mx((arr[ar][ac] | arr[br][bc]) - {t})[0]
            else:
                if t in arr[ar][ac]:
                    answer += v + find_mx(arr[br][bc])[0]
                else:
                    answer += v + find_mx(arr[ar][ac])[0]

        else:
            if arr[ar][ac]:
                answer += find_mx(arr[ar][ac])[0]
            if arr[br][bc]:
                answer += find_mx(arr[br][bc])[0]

    print(f'#{tc} {answer}')
