'''
1차땐 말이 중복으로 가지 않도록 cur을 짰었음 -> 시간 두 배 늘었다
'''
a = list(map(int, input().split()))
answer = 0
arr = [list(i for i in range(0, 41, 2)),  # 21 17 17 17 21
       [0] * 13 + [10, 13, 16, 19, 25],
       [0] * 14 + [20, 22, 24, 25],
       [0] * 13 + [30, 28, 27, 26, 25],  # 16는 4로
       [0] * 17 + [25, 30, 35, 40]]  # 21은 도착


def cur(depth, lst, acc):
    global answer
    if depth == 10:
        answer = max(answer, acc)
        return

    for i in range(4):
        # 도착하지 않은 말이면
        if lst[i][0] == 5:
            continue
        # 이동횟수만큼 이동
        cr, cc = lst[i]
        nr, nc = cr, cc + a[depth]
        # 파란 점이면 경로 바꾸기
        if nr == 0:
            if nc == 5:
                nr, nc = 1, 13
            elif nc == 10:
                nr, nc = 2, 14
            elif nc == 15:
                nr, nc = 3, 13
            elif nc == 20:
                nr = 4
        elif nr < 4 and 17 <= nc <= 20:
            nr = 4
        # 도착이면 나가기
        if nc > 20:
            lst[i] = (5, 0)
            cur(depth + 1, lst, acc)
            lst[i] = (cr, cc)
        else:
            # 누가 있으면 못 감
            if (nr, nc) in lst:
                continue
            lst[i] = (nr, nc)
            # 간 곳 점수 추가
            cur(depth + 1, lst, acc + arr[nr][nc])
            lst[i] = (cr, cc)


cur(0, [(0, 0), (0, 0), (0, 0), (0, 0)], 0)
print(answer)