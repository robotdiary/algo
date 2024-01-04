arr = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

bingo = 0
for idx in range(25):
    # 번호 1개를 부르면
    num = nums[idx]
    # 그 번호의 위치를 기준으로 +자가 빙고인지 확인
    for i in range(5):
        if num in arr[i]:
            j = arr[i].index(num)
            arr[i][j] = 0
            if not sum(arr[i]):
                bingo += 1
            if not sum([arr[0][j], arr[1][j], arr[2][j], arr[3][j], arr[4][j]]):
                bingo += 1
            if i == j and not sum([arr[0][0], arr[1][1], arr[2][2], arr[3][3], arr[4][4]]):
                bingo += 1
            if i + j == 4 and not sum([arr[0][4], arr[1][3], arr[2][2], arr[3][1], arr[4][0]]):
                bingo += 1
            if bingo >= 3:
                print(idx + 1)
                exit(0)
            break
