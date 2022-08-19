# 1979. 어디에 단어가 들어갈 수 있을까 (D2)
def puz_cnt(puz_squre, k_num):
    cnt = 0
    for i in range(1, n+1):
        for j in range(n+1-k):
            if puz_squre[i][j] == 0 and puz_squre[i][j+k+1] == 0 and puz_squre[i][j+1:j+k+1] == [1] * k_num:
                # 마지막 조건(1인지 찾는 것) > puz_squre[i][j+1:j+k+1]이라고만 하면 하나만 1 이어도 출력
                #                            puz_squre[i][j+1:j+k+1] = [1, 1, 1]은 k = 2일 때, 실패, 변수를 잘 생각하자
                cnt += 1
    return cnt


# [1] 자료 구조화
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [[0] * (n + 2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(n)] + [[0] * (n + 2)]
#        [[0] * n+2] 곱하기를 먼저하지 바보야
    z_puz = list(map(list, zip(*puzzle))) # zip(*puzzle)은 젤리 / list(zip(*puzzle))은 튜플리스트

    print(f'#{tc}', puz_cnt(puzzle, k) + puz_cnt(z_puz, k))
    # print(z_puz, puz_cnt(z_puz, k))

# [0, 1, 2, 3, 4, 5, 0]
# [0][1][2][3][4][5][6] range(7)
#    [1]            [6] range(1, 7)
#    [1]         [5]    range(1, n+1-k+1)