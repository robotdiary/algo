def solution():
    global answer
    visited = {arr[i][j]}
    cr, cc = i, j
    left = (cr + d1, cc - d1)
    right = (cr + d2, cc + d2)
    bottom = (cr + d1 + d2, cc - d1 + d2)
    d = 0
    while d < 4:
        nr, nc = cr + di[d], cc + dj[d]
        if (nr, nc) == (i, j):
            answer = max(answer, len(visited))
            return
        if arr[nr][nc] in visited:
            return
        visited.add((arr[nr][nc]))
        if (nr, nc) in {left, right, bottom, (i, j)}:
            d += 1
        cr, cc = nr, nc


di = (1, 1, -1, -1)
dj = (1, -1, -1, 1)
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-2):
        for j in range(1, N-1):
            for d1 in range(1, j + 1):
                for d2 in range(1, N-j):
                    if i + d1 + d2 >= N:
                        continue
                    if (d1 + d2) * 2 <= answer:
                        continue
                    solution()
    if answer < 2:
        answer = -1
    print(f'#{tc} {answer}')


