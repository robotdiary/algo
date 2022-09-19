# 12368. 24시간 D3
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    # 24시간이 안 넘었으면 숫자 그대로가 시간
    time = a + b
    # 24시간이 넘었으면 24를 계속 빼서 24보다 작게 만든다
    while time > 24:
        time -= 24
    # 24와 같을 때는 0시이다.
    if time == 24:
        time = 0
    print(f'#{tc} {time}')
