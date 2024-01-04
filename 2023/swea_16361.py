t = 10
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(input().strip()) for _ in range(8)]

    answer = 0
    for i in range(8):
        for j in range(8):
            w, h = 1, 1
            for k in range(n // 2):
                if j <= 8 - n:
                    if w and arr[i][j+k] != arr[i][j + n - 1 - k]:
                        w = 0
                else: w = 0
                if i <= 8 - n:
                    if h and arr[i + k][j] != arr[i + n - 1 - k][j]:
                        h = 0
                else: h = 0
            answer += w + h
    print(f'#{tc} {answer}')