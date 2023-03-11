# 종이의 개수
def mollu(length, x, y):  # 길이, 시작점           3, 6, 0
    for r in range(x, x + length, length//3):      # 3, 3, 1 -> 0, 3, 6
        for c in range(y, y + length, length//3):  # 0, 3, 1 -> 0, 3, 6
            check_num = arr[r][c]              # arr[6][0]
            def_flag = 0
            # print('check_num', check_num)
            for inner_i in range(length//3):      # 3 -> 0, 1, 2
                for inner_j in range(length//3):  # 3 -> 0, 1, 2
                    # print('돌고있는 자리', arr[r + inner_i][c + inner_j])
                    if arr[r + inner_i][c + inner_j] != check_num:
                        mollu(length//3, r, c)  # 3, 6, 0
                        def_flag = 1
                        break
                if def_flag:
                    break
            else:
                count_dict[check_num] += 1
                # print('답: ', count_dict)


count_dict = {-1: 0, 0: 0, 1: 0}
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
first_num = arr[0][0]

flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != first_num:
            mollu(n, 0, 0)
            flag = 1
            break
    if flag:
        break
else:
    count_dict[first_num] += 1
print(count_dict[-1])
print(count_dict[0])
print(count_dict[1])
