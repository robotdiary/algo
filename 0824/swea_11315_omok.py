T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    zip_arr = list(map(list, zip(*arr)))
    result = 0
    print(arr)
    for i in range(n): # 모든 줄은 다 봐야함
        for j in range(n-4):
            if arr[i][j] == 'o':
                if arr[i][j:j+5] == 'o' * 5:
                    result = 'YES'
                elif zip_arr[j][i:i+5] == 'o' * 5:
                    result = 'YES'
    for
