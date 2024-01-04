for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    a = input()

    nums = set()
    for i in range(N):
        num = ''
        for j in range(N//4):
            num += a[(i + j) % N]
        nums.add(int(num, 16))

    answer = sorted(list(nums), reverse=True)[K-1]
    print(f'#{tc} {answer}')
