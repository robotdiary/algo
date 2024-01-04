# 카잉 달력
for tc in range(int(input())):
    m, n, x, y = map(int, input().split())
    start = [x, x]
    if x > n:
        if x % n:
            start = [x, x % n]  # 실제로 올라가는 변수
        else:
            start = [x, n]
    now = [start[0], start[1]]
    visited = set()  # 원래대로 돌아오면 나갈 수 있도록 체크
    acc = m - n  # 바뀌는 y값
    flag = 1
    answer = x
    while flag:
        # 원하는 날이면 종료
        if now == [x, y]:
            flag = 0
            break
        # 종말의 날이거나 한바퀴 돌았으면 종료
        if now == [m, n]:
            break
        if (now[1] + acc) % n:
            now[1] = (now[1] + acc) % n
        else:
            now[1] = n
        # 한바퀴 돌면 종료
        if now == start:
            break
        answer += m

    if flag:
        print(-1)
    else:
        print(answer)
