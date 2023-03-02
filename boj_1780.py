# 종이의 개수
def mollu(length, x, y):  # 길이, 시작점
    for rc in range(9):
        check_num = arr[x][y]
        flag = 0
        for i in range(length//3):
            for j in range(length//3):
                if arr[x + rc//3][y + rc % 3 * (length // 3)] != check_num:
                    mollu(length//3, x + rc//3, y + rc % 3 * (length // 3))
                    return
        else:
            count_dict[check_num] += 1


count_dict = {-1: 0, 0: 0, 1: 0}
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mollu(n, 0, 0)
print(count_dict)