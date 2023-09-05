def cnt(depth, maxdice, lst):
    if depth == 10:
        solve(lst)
        return
    if maxdice > 4:
        maxdice = 4
    for i in range(maxdice):
        if i + 1 == maxdice:
            cnt(depth + 1, maxdice + 1, lst + [i])
        else:
            cnt(depth + 1, maxdice, lst + [i])


def solve(lst):
    global answer
    mal = [[0, 0], [0, 0], [0, 0], [0, 0]]
    goal = [0] * 4
    acc = 0
    for i in range(10):
        # 아직 골인 안 했고, 그 위치에 다른 말이 없으면 갈 수 있음
        if goal[lst[i]]:
            return
        mal[lst[i]][1] += dice[i]

        if mal[lst[i]][1] > 20:
            goal[lst[i]] = 1
            if sum(goal) == 4:
                answer = max(answer, acc)
                return
            continue
        elif mal[lst[i]] == [0, 5]:
            mal[lst[i]] = [1, 13]
        elif mal[lst[i]] == [0, 10]:
            mal[lst[i]] = [2, 14]
        elif mal[lst[i]] == [0, 15]:
            mal[lst[i]] = [3, 13]
        elif mal[lst[i]] == [0, 20]:
            mal[lst[i]] = [4, 20]
        elif 4 > mal[lst[i]][0] > 0 and mal[lst[i]][1] > 16:
            mal[lst[i]][0] = 4
        if mal.count(mal[lst[i]]) > 1:
            return
        acc += arr[mal[lst[i]][0]][mal[lst[i]][1]]
    answer = max(answer, acc)


arr = [list(range(0, 41, 2)),
       [0]*13 + [10, 13, 16, 19, 25, 30, 35, 40],
       [0]*14 + [20, 22, 24, 25, 30, 35, 40],
       [0]*13 + [30, 28, 27, 26, 25, 30, 35, 40],
       [0]*17 + [25, 30, 35, 40]]
        # 21칸 == 나감
        # 5, 10, 15일 때 r + 1
        # 13으로, 14로, 13으로
dice = list(map(int, input().split()))
answer = 0

cnt(0, 1, [])
print(answer)