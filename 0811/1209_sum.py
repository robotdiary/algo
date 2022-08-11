# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(map(list, zip(*list1))))

for T in range(1, 11):
    tc = input()
    line = [list(map(int, input().split())) for _ in range(100)]
    column = list(map(list, zip(*line)))
    maxnum = 0
    right_down = []
    left_down = []
    for i in range(100):
        if sum(line[i]) > maxnum:
            maxnum = sum(line[i])
        if sum(column[i]) > maxnum:
            maxnum = sum(column[i])
        right_down.append(line[i][i])
        left_down.append(line[i][99-i])
    if sum(right_down) > maxnum:
        maxnum = sum(right_down)
    if sum(left_down) > maxnum:
        maxnum = sum(left_down)
    print(f'#{tc} {maxnum}')