T = int(input())
for tc in range(1, T+1):
    n = int(input())
    number = list(map(int, input().split()))
    sortnum = sorted(number)
    answer = []
    for i in range(n//2):
        answer.append(sortnum[-1-i])
        answer.append(sortnum[i])
    if n % 2:
        answer.append(number[n//2])
    print(f'#{tc} {answer}')