di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            flower = arr[i][j]
            for d in range(4):
                if 0 <= i + di[d] < n and 0 <= j + dj[d] < m:
                    flower += arr[i + di[d]][j + dj[d]]
            answer = max(answer, flower)

    print(f'#{tc} {answer}')
