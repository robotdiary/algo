# 2805 농작물 수확하기 (D3)
T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 농장의 크기
    arr = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    for i in range(n // 2 + 1):
        if i == n // 2:
            cnt += sum(arr[i])
        else:
            cnt += sum(arr[i][n // 2 - i:n // 2 + i + 1])
            cnt += sum(arr[n - 1 - i][n // 2 - i:n // 2 + i + 1])
    print(f'#{tc} {cnt}')