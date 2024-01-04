def snail(cnt, x, y, acc, d):
    if cnt:
        for i in range(cnt):
            x += di[d % 4]
            y += dj[d % 4]
            arr[x][y] = acc
            acc += 1
        d += 1
        for i in range(cnt):
            x += di[d % 4]
            y += dj[d % 4]
            arr[x][y] = acc
            acc += 1
        snail(cnt - 1, x, y, acc, d + 1)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(range(1, n + 1))] + [[0] * n for _ in range(n-1)]

    snail(n - 1, 0, n - 1, n + 1, 1)

    print(f'#{tc}')
    for gogo in arr:
        print(*gogo)