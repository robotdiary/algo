# 13547. 팔씨름 D3
T = int(input())
for tc in range(1, T + 1):
    s = input()
    lose = 0
    for i in s:
        if i == 'x':
            lose += 1
    answer = 'YES'
    if lose >= 8:
        answer = 'NO'
    print(f'#{tc} {answer}')