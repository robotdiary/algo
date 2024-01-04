for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = []

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            target = arr[i][j]
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if target <= arr[i + dr][j + dc]:
                    break
            else:
                answer.append(target)

    if len(answer) > 1:
        print(f'#{tc} {max(answer) - min(answer)}')
    else:
        print(f'#{tc} -1')
