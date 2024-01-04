def work(depth, acc):
    global answer
    if depth == n:
        answer = max(answer, acc)
        return

    if depth + tp[depth][0] <= n:
        work(depth + tp[depth][0], acc + tp[depth][1])
    work(depth + 1, acc)


n = int(input())
tp = list(tuple(map(int, input().split())) for _ in range(n))
answer = 0
work(0, 0)
print(answer)