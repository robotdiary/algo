# 1961. 숫자 배열 회전 (D2)
def turn90(arrlst, w):
    newarr = [[0] * w for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newarr[j][n-1-i] = arrlst[i][j]
    return newarr


T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n*n배열
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    answer1 = turn90(arr, n)
    answer2 = turn90(answer1, n)
    answer3 = turn90(answer2, n)
    print(f'#{tc}')
    for i in range(n):
        print(''.join(map(str, answer1[i])), ''.join(map(str, answer2[i])), ''.join(map(str, answer3[i])))