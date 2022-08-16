T = int(input())
for tc in range(1, T+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    num = 1
    cnt = n # 4
    now = [0, -1]
    while cnt > 0:
        for _ in range(cnt): # 4
            snail[now[0]][now[1] + 1] = num
            num += 1
            now[1] += 1
        cnt -= 1
        if cnt == 0:
            break
        for _ in range(cnt): # 3
            snail[now[0] + 1][now[1]] = num
            num += 1
            now[0] += 1
        for _ in range(cnt): # 3
            snail[now[0]][now[1] - 1] = num
            num += 1
            now[1] -= 1
        cnt -= 1
        if cnt == 0:
            break
        for _ in range(cnt): # 2
            snail[now[0] - 1][now[1]] = num
            num += 1
            now[0] -= 1
    print(f'#{tc}')
    for i in range(n):
        print(*snail[i])