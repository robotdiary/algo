'''
ogu님 코드 봤다.
시작 방향을 네 방향으로 지정해서 도는 거 너무 어려운데
        arr = [[arr[N-1-i][j] for i in range(N)] for j in range(N)]
이 코드로 배열을 쉽게 90도 회전 시킬 수 있다.
배열을 돌리면 네 방향으로 시작하지 않고, 한쪽 방향으로만 확인 할 수 있다.
'''
def gravity(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        idx = 0
        for j in range(N):
            if arr[i][j]:
                new_arr[i][idx] = arr[i][j]
                idx += 1
    # print('중력작용')
    # print(*new_arr, sep='\n')
    return new_arr


def crush(arr):
    new_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j+1 < N and arr[i][j] == arr[i][j+1]:
                new_arr[i][j] = arr[i][j] * 2
                arr[i][j + 1] = 0
            else:
                new_arr[i][j] = arr[i][j]

    # print('부딪히기')
    # print(*new_arr, sep='\n')
    return new_arr


def cur(depth, arr):
    global answer
    if depth == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > answer:
                    answer = arr[i][j]
        return

    for i in range(4):
        arr = [[arr[N-1-i][j] for i in range(N)] for j in range(N)]
        cur(depth + 1, gravity(crush(gravity(arr))))


N = int(input())
answer = 0
# print()
cur(0, [list(map(int, input().split())) for _ in range(N)])
print(answer)