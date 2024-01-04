def turn(acc, idx, time):
    global answer
    if not time or idx >= n:
        answer = max(answer, acc)
        return
    if idx + 2 <= n:
        turn(acc // 2 + lst[idx + 2], idx + 2, time - 1)
    if idx + 1 <= n:
        turn(acc + lst[idx + 1], idx + 1, time - 1)


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    lst = [1] + list(map(int, input().split()))
    answer = 0
    turn(1, 0, m)
    print(f'#{tc} {answer}')