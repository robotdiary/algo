def game(depth, acc, maxdice):
    global answer
    # print(depth, 'mal 현황 : ', mal, acc)
    if depth == 10:
        answer = max(answer, acc)
        return
    if maxdice > 4:
        maxdice = 4
    for i in range(maxdice):
        # print(maxdice, '번 중', i + 1, '번', depth, '번째 주사위', '합계: ', acc)
        # 이미 끝난 말이면 지나가
        if mal[i][1] > 20:
            continue
        old = mal[i][1] * 1  # 되돌리 원래 변수
        mal[i][1] += dice[depth]
        # 도착 지점이면 acc없이 다음 뎁스로
        if mal[i][1] > 20:
            if i + 1 == maxdice:
                game(depth + 1, acc, maxdice + 1)
            else:
                game(depth + 1, acc, maxdice)
            mal[i][1] -= dice[depth]
            continue
        elif mal[i] == [0, 5]:
            mal[i] = [1, 13]
        elif mal[i] == [0, 10]:
            mal[i] = [2, 14]
        elif mal[i] == [0, 15]:
            mal[i] = [3, 13]
        elif mal[i] == [0, 20]:
            mal[i] = [4, 20]
        elif 4 > mal[i][0] > 0 and mal[i][1] > 16:
            mal[i][0] = 4
        # 갈 자리에 있으면 스킵
        if mal.count(mal[i]) > 1:
            continue
        if i + 1 == maxdice:
            game(depth + 1, acc + arr[mal[i][0]][mal[i][1]], maxdice + 1)
        else:
            game(depth + 1, acc + arr[mal[i][0]][mal[i][1]], maxdice)
        mal[i][1] = old


arr = [list(range(0, 41, 2)),
       [0]*13 + [10, 13, 16, 19, 25, 30, 35, 40],
       [0]*14 + [20, 22, 24, 25, 30, 35, 40],
       [0]*13 + [30, 28, 27, 26, 25, 30, 35, 40],
       [0]*17 + [25, 30, 35, 40]]
        # 21칸 == 나감
        # 5, 10, 15일 때 r + 1
        # 13으로, 14로, 13으로
mal = [[0, 0], [0, 0], [0, 0], [0, 0]]
dice = list(map(int, input().split()))
answer = 0

# cnt(0, 1, [])
game(0, 0, 1)
print(answer)