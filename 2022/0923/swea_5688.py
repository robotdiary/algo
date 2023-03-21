# 5688. 세제곱근을 찾아라 D3
for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = 0
    answer = n ** (1/3)
    ans = round(answer)
    if ans ** 3 == n:
        answer = ans
    else:
        answer = -1
    print(f'#{tc} {answer}')