import sys
sys.stdin = open('input.txt')

for T in range(10):
    tc = int(input())
    ladder = ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    x = 98
    y = ladder[-1].index(2) # 2의 조ㅏ표
    dr = [0, 0, -1] # 좌 우 위
    dc = [-1, 1, 0]
    while x > 0:
        for i in range(3):
            if ladder[x+dr[i]][y+dc[i]]:
                x += dr[i]
                y += dc[i]
                if i == 0:
                    while ladder[x][y-1]:
                        y -= 1
                    x -= 1
                    break
                elif i == 1:
                    while ladder[x][y+1]:
                        y += 1
                    x -= 1
                    break
                # else:
                #     while ladder[x-1][y-1] == 0 and ladder[x-1][y+1] == 0:
                #         x += 1
                #     break
    print(f'#{tc} {y-1}')