for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(m):
            flowers = arr[i][j]
            for k in range(1, arr[i][j] + 1):  # 곱하는 값 0부터면 안 되지
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = i + (dr * k)
                    nc = j + (dc * k)
                    if 0 <= nr < n and 0 <= nc < m:
                        flowers += arr[nr][nc]
            answer = max(answer, flowers)
    print(f'#{tc} {answer}')