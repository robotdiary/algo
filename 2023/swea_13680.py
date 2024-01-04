for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    arr = [[0] * (n + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 2)]
    zip_arr = list(zip(*arr))

    answer = 0
    for i in range(1, n + 1):
        for j in range(1, n-k+2):
            if arr[i][j-1:j+k+1] == [0] + [1]*k + [0]:
                answer += 1
            if zip_arr[i][j-1:j+k+1] == tuple([0] + [1]*k + [0]):
                answer += 1

    print(f'#{tc} {answer}')
