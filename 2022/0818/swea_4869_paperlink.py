def dp(n):
    global count
    if n >= 3 and n >= len(count):
        count.append(dp(n-1) + dp(n-2) * 2)
    return count[n]


count = [0, 1, 3]
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {dp(int(input()) // 10)}') # / 10 하면 .0으로 float으로 나옴