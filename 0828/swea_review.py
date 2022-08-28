# 1289 원재의 메모리 복구하기(D3)
# T = int(input())
# for tc in range(1, T + 1):
#     memory = map(int, input())
#     check = 0
#     cnt = 0
#     for i in memory:
#         if i != check:
#             cnt += 1
#             check = i
#     print(f'#{tc} {cnt}')

# 1206 View(D3)
# T = 10
# for tc in range(1, T + 1):
#     n = int(input())
#     buildings = list(map(int, input().split()))
#     answer = 0
#     for i in range(2, len(buildings)-2):
#         side = [buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2]]
#         if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
#             answer += buildings[i] - max(side)
#     print(f'#{tc} {answer}')

# 1216 회문2 40분
# def check(arr):
#     global answer
#     for i in range(100):
#         for j in range(99):
#             if j > 100 - answer:
#                 break
#             for z in range(99, j, -1):
#                 if arr[i][j] == arr[i][z] and z - j + 1 > answer:
#                     cnt = 0
#                     left = j
#                     right = z
#                     while left < right:
#                         if arr[i][left] == arr[i][right]:
#                             cnt += 2
#                             left += 1
#                             right -= 1
#                         else:
#                             cnt = 0
#                             break
#                     if cnt and (z - j + 1) % 2:
#                         cnt += 1
#                     if cnt > answer:
#                         answer = cnt
#                 elif z - j + 1 < answer:
#                     break
#     return
#
# T = 10
# for tc in range(1, T + 1):
#     _ = input()
#     pal = [list(input()) for _ in range(100)]
#     zip_pal = list(map(list, zip(*pal)))
#     answer = 0
#     # 가로 검사
#     check(pal)
#     check(zip_pal)
#
#     print(f'#{tc} {answer}')

# 1961 숫자배열회전(D2) 16분
# def turn(item):
#     answer = [[0] * n for _ in range(n)]
#     for i in range(n): # 0, 1, 2
#         for j in range(n): # 0, 1, 2
#             answer[j][n-1-i] = str(item[i][j]) # i = 0 j = 0
#     return answer
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     answer90 = turn(arr)
#     answer180 = turn(answer90)
#     answer270 = turn(answer180)
#     print(f'#{tc}')
#     for i in range(n):
#         print(''.join(answer90[i]), ''.join(answer180[i]), ''.join(answer270[i]))

# GRAVITY
