T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i): # 0부터 i-1 까지 보고싶으니까 0, i를 써야지
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    result = a[-1] - a[0]
    print(f'#{t} {result}')