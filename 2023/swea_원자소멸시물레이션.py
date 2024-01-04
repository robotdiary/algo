from collections import deque
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arrow = {0: [], 1: [], 2: [], 3: []}
    power = {0: [], 1: [], 2: [], 3: []}
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        arrow[d].append((y * 2, x * 2))
        power[d].append(k)

    for cr, cc in arrow[2]:
        for i in range(4000 - cr):

    # 위 아래 따로 확인

    print(f'#{tc} {answer}')