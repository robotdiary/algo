'''
안 해
'''
def get_point(arr):
    point = 0
    gravity(arr)
    for i in range(100):
        if arr[i].count(0) == 0:
            point += 1
            arr[i] = [0] * 4
    gravity(arr)
    return point


def gravity(arr):
    for i in range(N-2, -1, -1):
        for j in range(3):
            cr, cc = i, j
            while cr < N-1 and arr[cr+1][cc] == 0:
                arr[cr][cc], arr[cr + 1][cc] = arr[cr + 1][cc], arr[cr][cc]
                cr += 1


def cur(depth, arr, acc):
    # 블럭 열 정하기
    C = [blocks[depth][1]]
    if C[0] == -1:
        C = [0, 1, 2, 3]

    for c in C:
        point = acc
        new_arr = [arr[i] for i in range(100)]
        # 블럭 행 정하기
        for r in range(99, -1, -1):
            if new_arr[r][c] == 0:
                new_arr[r][c] = blocks[depth[0]]
                break
        point += get_point(new_arr)



N = int(input())
direction = {i: list(map(lambda x: int(x)-1, input().split())) for i in range(1, 9)}
blocks = list(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N))  # 종류(1-8), 위치 -1몰라 0-3

bucket = [[0] * 4 for _ in range(100)]
answer = 0

# [1] 블럭 위치 정하기
# 정해져 있으면 떨어지고
# 안 정해져 있으면
    # 깰 수 있으면 거기 떨어지고, 아니면 움직인 후 깨지는 자리에 넣어야 함

# [2] 중력 + 줄 확인해서 점수 획득 + 중력

# [3] 이동 (new_arr 같은 위치는 작은 숫자 살아남기)

# [4] 중력 + 줄 확인해서 점수 획득 + 중력

