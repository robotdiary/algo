T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    counts = [0] * 10
    result = 0
    maxcard = 0
    for i in range(N):
        counts[cards[i]] += 1
    for j in range(9, -1, -1):
        if counts[j] > result:
            result = counts[j]
            maxcard = cards[j] # 같은 개수가 여러개면 큰 수 출력
    print(f'#{tc} {maxcard} {result}')