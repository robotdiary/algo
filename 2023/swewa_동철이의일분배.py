def working(depth, acc):
    global answer
    if not depth:
        answer = max(answer, acc)
        return

    if acc * arr[depth - 1][i] > answer:
        working(depth - 1, acc * arr[depth - 1][i])
    working(depth, acc)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [0] * n
    answer = 0
    working(n, 100)
    print(f'#{tc} {answer:.6f}')