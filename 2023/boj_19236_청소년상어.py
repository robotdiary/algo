arr = [[0] * 4 for _ in range(4)]
info = {}
for i in range(4):
    ir = list(map(int, input().split()))
    for j in range(4):
        info[ir[j * 2]] = [i, j, ir[j * 2 + 1]]
        arr[i][j] = ir[j * 2]
answer = 0
first = arr[0][0]
info[0] = [0, 0, info[arr[0][0]][2]]
arr[0][0] = 0
di = (-1, -1, -1, 0, 1, 1, 1, 0)
dj = (1, 0, -1, -1, -1, 0, 1, 1)
stack = [(info, arr, first, {first})]
while stack:
    fish_info, table, acc, eat = stack.pop()
    for i in range(1, 17):
        if i not in eat:
            for turn in range(8):
                cr, cc, d = fish_info[i]
                d %= 8
                nr, nc = cr + di[d], cc + dj[d]
                if not 0 <= nr < 4 or not 0 <= nc < 4 or (nr, nc) == (fish_info[0][0], fish_info[0][1]):
                    fish_info[i][2] += 1
                else:
                    table[cr][cc], table[nr][nc] = table[nr][nc], table[cr][cc]
                    fish_info[i] = [nr, nc, d]
                    if table[cr][cc]:
                        fish_info[table[cr][cc]] = [cr, cc, fish_info[table[cr][cc]][2]]
                    break
    # 상어 이동
    flag = 0
    cr, cc, d = fish_info[0]
    nr, nc = cr + di[d], cc + dj[d]
    while 0 <= nr < 4 and 0 <= nc < 4:
        if table[nr][nc]:
            new_fish = dict()
            new_fish[0] = [nr, nc, fish_info[table[nr][nc]][2]]
            # table 위치 바꾸기
            new_table = [[0] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    if table[i][j]:
                        new_fish[table[i][j]] = [i, j, fish_info[table[i][j]][2]]
                        new_table[i][j] = table[i][j]
            new_table[nr][nc] = 0
            stack.append((new_fish, new_table, acc + table[nr][nc], eat | {table[nr][nc]}))
            flag = 1

        nr += di[d]
        nc += dj[d]
    if not flag:
        answer = max(answer, acc)
print(answer)

