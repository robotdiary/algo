# 9386 연속한 1의 개수 (D1)
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input()))
    answer = 0
    cnt = 0
    for i in numbers:
        if i == 1:
            cnt += 1
            if cnt > answer:
                answer = cnt
        else:
            cnt = 0
    print(f'#{tc} {answer}')