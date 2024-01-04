'''
tc9 틀림 :: 다 지우고 다시 짜보자
문 두개로는 전체 조합으로 사람 나누기
도착 시간 별로 sort -> 세칸앞 [idx-3]에서 도착 시간, 지연 시간 확인 가능
'''


def cur(depth, A, B, start):
    if depth == len(mans):
        solve(A, B)
        return

    for select in range(start, len(mans)):
        cur(depth + 1, A + [stair1[depth][::]], B, select + 1)
        cur(depth + 1, A, B + [stair2[depth][::]], select + 1)


def solve(a, b):
    global answer
    # print('도착 모음')
    a.sort()
    b.sort()
    result1 = [(0, 0), (0, 0), (0, 0)]
    result2 = [(0, 0), (0, 0), (0, 0)]
    for ai in range(len(a)):
        지연 = 0
        if a[ai][0] < result1[ai][1]:
            지연 = result1[ai][1] - a[ai][0]
        result1.append((a[ai][0] + 지연, a[ai][1] + 지연))
    for ai in range(len(b)):
        지연 = 0
        if b[ai][0] < result2[ai][1]:
            지연 = result2[ai][1] - b[ai][0]
        result2.append((b[ai][0] + 지연, b[ai][1] + 지연))
    # print(a)
    # print(b)
    # print(result1)
    # print(result2)
    answer = min(answer, max(result1[-1][1] + 1, result2[-1][1] + 1))


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 1사람 2~계단길이

    mans = []
    doors = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                mans.append((i, j))
            elif arr[i][j] >= 2:
                doors.append((i, j, arr[i][j]))

    stair1 = []
    stair2 = []
    for man in range(len(mans)):
        dist1 = (abs(mans[man][0] - doors[0][0]) + abs(mans[man][1] - doors[0][1]))
        dist2 = (abs(mans[man][0] - doors[1][0]) + abs(mans[man][1] - doors[1][1]))
        stair1.append((dist1, dist1 + doors[0][2]))
        stair2.append((dist2, dist2 + doors[1][2]))

    answer = 99999
    cur(0, [], [], 0)
    print(f'#{tc} {answer}')











# def cur(depth, left, right, start):
#     if depth == idx - 1:
#         solve(left, right)
#         return
#
#     for i in range(start, idx):
#         cur(depth + 1, left+[door1[i]], right, i + 1)
#         cur(depth + 1, left, right + [door2[i]], i + 1)
#
#
# def bfs(x, y, k, d):
#     for idx in range(len(mans)):
#         cr, cc = mans[idx]
#         dist = abs(cr - x) + abs(cc - y)
#         d[idx + 1] = [dist, dist + k + 1]
#
#
# def solve(left, right):
#     global answer
#     left = sorted(left)
#     right = sorted(right)
#
#     stair1 = [[0, 0], [0, 0], [0, 0]]
#     stair2 = [[0, 0], [0, 0], [0, 0]]
#     for l in range(len(left)):
#         대기 = 0
#         if stair1[l][1] > left[l][0]:
#             대기 = stair1[l][1] - left[l][0]
#         stair1.append((left[l][0] + 대기, left[l][1] + 대기))
#         if stair1[-1][1] >= answer:
#             return
#
#     for l in range(len(right)):
#         대기 = 0
#         if stair2[l][1] > right[l][0]:
#             대기 = stair2[l][1] - right[l][0]
#         stair2.append((right[l][0] + 대기, right[l][1] + 대기))
#         if stair2[-1][1] >= answer:
#             return
#
#     time = max(stair1[-1][1], stair2[-1][1])
#     answer = min(answer, time)
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(input().split()) for _ in range(N)]  # 문자열
#     # 1사람 2~계단길이
#
#     # [0] 계단 위치 찾기
#     doors = []
#     mans = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '1':
#                 mans.append((i, j))
#             elif arr[i][j] != '0':
#                 doors.append((i, j, int(arr[i][j])))
#
#     # [0] 계단과 사람 사이 거리 딕셔너리 만들기
#     door1 = {}
#     door2 = {}  # (도착 시간, 떠나는 시간)
#     bfs(*doors[0], door1)
#     bfs(*doors[1], door2)
#
#     idx = len(mans) + 1
#     selected = [0] * idx
#
#     answer = 999999
#     # [1] 사람 조합 찾기
#     cur(0, [], [], 1)
#
#     print(f'#{tc} {answer}')
