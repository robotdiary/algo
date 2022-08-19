# # 1974. 스도쿠 검증 (D2)
# 가로, 세로에 1~9까지 하나씩 전부 있는지 확인하는 함수, set으로 중복값을 제거한 후 9개인지 확인
def line_sudoku(sdk_lst):
    for i in sdk_lst:
        if len(set(i)) != 9: # 아닌게 있으면 바로 함수를 종료하므로 불필요한 검사 하지 않음
            return 0
    else: # for문을 전부 통과했을 때만 실행된다.
        return 1

# 네모의 값들을 더했을 때 45인지 확인하는 함수
def nemo_sudoku(sdk_lst):
    for i in range(0, 7, 3): # 0, 3, 6
        for j in range(0, 7, 3): # 0, 3, 6 인덱스로 아홉번(3 * 3) 반복할 것임
            if sum(sdk_lst[i][j:j+3] + sdk_lst[i+1][j:j+3] + sdk_lst[i+2][j:j+3]) != 45:
                return 0
        else:
            return 1


T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    zip_sudoku = list(map(list, zip(*sudoku)))

# 셋 다 정답인 1이 return 되었다면 1, 하나라도 0이면 0
    if line_sudoku(sudoku) and line_sudoku(zip_sudoku) and nemo_sudoku(sudoku):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


# for i in range(0, 7, 3):
#     print(i)
# sdk_lst = [list(map(int, input().split())) for _ in range(9)]
# for i in range(0, 7, 3):
#     for j in range(0, 7, 3):
#         print(sdk_lst[i][j:j + 3] + sdk_lst[i + 1][j:j + 3] + sdk_lst[i + 2][j:j + 3])

