# # 2382. [모의 SW 역량테스트] 미생물 격리
from collections import defaultdict
d = {
    1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)
}
turn = {
    1: 2, 2: 1, 3: 4, 4: 3
}
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())  # 크기, 시간, 군집수
    arr = [[0] * n for _ in range(n)]
    for i in range(k):
        r, c, nums, run = map(int, input().split())
        arr[r][c] = (r, c, nums, run)
    goto = defaultdict()
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                goto[(r+d[arr[i][j][3]][0], c+d[arr[i][j][3]][1])] = (arr[i][j][2], arr[i][j][3])
    for i in range(len(goto)-1):
        for j in range(i + 1, len(goto)):



# [2] 옮길 것을 적어놓고, 다 완성하고 올리자


# [1] 배열에 바로 수정하니까, 모든 이동을 적을 수 없음.
# d = {
#     '1': (-1, 0), '2': (1, 0), '3': (0, -1), '4': (0, 1)
# }
# turn = {
#     '1': '2', '2': '1', '3': '4', '4': '3'
# }
# T = int(input())
# for tc in range(1, T + 1):
#     n, m, k = map(int, input().split()) # 크기, 시간, 군집수
#     arr = [[0] * n for _ in range(n)]
#     for i in range(k):
#         r, c, nums, run = map(int, input().split())
#         arr[r][c] = [nums, str(run)]
#     # [1] 시간만큼 반복
#     while m:
#         # [2] 전체를 돌면서
#         for i in range(n):
#             stop = False
#             for j in range(n):
#                 if stop:
#                     stop = False
#                     continue
#                 if arr[i][j]:
#                 # [3] 나아갈 방향
#                     if arr[i][j][1] == 4:
#                         stop = True
#                     nr = i + d[arr[i][j][1]][0] # 5 + 0 = 5
#                     nc = j + d[arr[i][j][1]][1] # 1 + 1 = 2
#                     # [4] 갈 곳에 누가 있으면, 더하기
#                     if arr[nr][nc]:
#                         arr[nr][nc] += arr[i][j]
#                         arr[i][j] = 0
#                     # [5] 갈 곳이 0이면 자리 바꾸기
#                     else:
#                         arr[i][j], arr[nr][nc] = arr[nr][nc], arr[i][j]
#         # 한 군데에 여러 애가 있으면, 계산
#         for i in range(n):
#             for j in range(n):
#                 if arr[i][j] and len(arr[i][j]) > 3:
#                     bugs = []
#                     for z in range(0, len(arr[i][j]), 2):
#                         bugs.append(arr[i][j][z])
#                     arr[i][j] = [sum(bugs), arr[i][j][arr[i][j].index(max(bugs)) + 1]]
#
#                 # [6] 약품에 닿으면 방향 바꾸고 미생물 감소
#                 if arr[i][j]:
#                     if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#                     # 반대방향, 미생물 // 2, 미생물이 1 이하면 삭제
#                         arr[i][j][1] = turn[arr[i][j][1]]
#                         arr[i][j][0] //= 2
#                         if arr[i][j][0] < 2:
#                             arr[i][j] = 0
#         # print(arr)
#
#         m -= 1
#
#     answer = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j]:
#                 answer += arr[i][j][0]
#     # print(f'#{tc} {answer}')
