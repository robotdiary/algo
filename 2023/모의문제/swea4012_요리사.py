def cur(depth, start, a):
    global answer
    if depth == N // 2:
        left, right = 0, 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if i in a and j in a:
                        left += arr[i][j]
                    elif i not in a and j not in a:
                        right += arr[i][j]

        answer = min(answer, abs(left - right))
        return

    for i in range(start, N):
        visited[i] = 1
        cur(depth + 1, i + 1, a + [i])
        visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    answer = 9999999
    cur(0, 0, [])

    print(f'#{tc} {answer}')