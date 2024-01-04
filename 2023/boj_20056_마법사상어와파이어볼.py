'''
1시간 23분
돌리기까지 구현 : 49분
테케 3맞까지 구현 : 14분
디버깅 : 20분
-----------------------
출력이 헷갈리면 어떻게 하지…?
돌면서 삭제하지 말자 다 돌고 해라
(1차) 출력 잘못함
(2차) 668 / 117156
'''
n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs.append((ri-1, ci-1, mi, si, di))

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
for tc in range(k):
    arr = [[[0, 0, 0, -1] for _ in range(n)] for _ in range(n)]  # 힘, 속도, 개수, 방향
    # print(arr)
    for fireball in range(len(fireballs)):
        cr, cc, m, s, d = fireballs.pop()
        # 새 위치 찾기
        nr, nc = (cr + (di[d] * s)) % n, (cc + (dj[d] * s)) % n
        # 이동시키기
        arr[nr][nc][0] += m
        arr[nr][nc][1] += s
        arr[nr][nc][2] += 1
        if arr[nr][nc][2] == 1:
            arr[nr][nc][3] = d
        # 지금까진 같았는데, 이제 달라졌으면
        elif arr[nr][nc][3] < 8 and arr[nr][nc][3] % 2 != d % 2:
            arr[nr][nc][3] = 8
        # 달랐으면 다른대로 납두고, 계속 같아도 놔두고

    for i in range(n):
        for j in range(n):
            # 파볼 1개면 그대로
            if arr[i][j][2] == 1:
                fireballs.append((i, j, arr[i][j][0], arr[i][j][1], arr[i][j][3]))
            # 두 개 이상이고, 나눠도 힘이 남아있으면
            elif arr[i][j][2] > 1 and arr[i][j][0] // 5:
                if arr[i][j][3] == 8:
                    for dest in range(1, 8, 2):
                        fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], dest))
                else:
                    for dest in range(0, 8, 2):
                        fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], dest))
# print(fireballs)
answer = 0
for ans in fireballs:
    answer += ans[2]
print(answer)

# def move(cr, cc, m, s, d):  # 좌표, 질량, 속도, 방향
#     # 새집 가기
#     if cr + (di[d] * s) >= 0:
#         nr = (cr + (di[d] * s)) % n
#     else:
#         nr = n - (abs(cr + (di[d] * s)) % n)
#     if cc + (dj[d] * s) >= 0:
#         nc = (cc + (dj[d] * s)) % n
#     else:
#         nc = n - (abs(cc + (dj[d] * s)) % n)
#     arr[nr][nc][0] += m
#     arr[nr][nc][1] += s
#     arr[nr][nc][2] += 1
#     if arr[nr][nc][3] == -1:
#         arr[nr][nc][3] = d
#     elif arr[nr][nc][3] % 2 != d % 2:
#         arr[nr][nc][3] = 2
#
#     # 있던 집 나가기
#     # arr[cr][cc] = [0, 0, 0, -1]
#
#
# n, m, k = map(int, input().split())  # n*n, 파이어볼수, 명령수
# fireballs = []
# for _ in range(m):
#     ri, ci, mi, si, di = map(int, input().split())
#     fireballs.append((ri - 1, ci - 1, mi, si, di))
#
# di = [-1, -1, 0, 1, 1, 1, 0, -1]
# dj = [0, 1, 1, 1, 0, -1, -1, -1]
#
# # 이동 명령을 내리면 fireballs.pop으로를 돌면서 이동시킨다
# for _ in range(k):
#     arr = [[[0, 0, 0, -1] for _ in range(n)] for _ in range(n)]  # 질량합, 속력합, 파이어볼수, 짝수0 홀수1 섞이면2
#     for _ in range(len(fireballs)):
#         move(*fireballs.pop())
#
# # 같은 좌표에 들어가면 (r, c, 질량//5, 속력//합쳐진개수, 방향)로 바꿔서
#     for i in range(n):
#         for j in range(n):
#             # 질량이 0보다 크면 fireballs.append
#             if arr[i][j][2] > 1 and arr[i][j][0] // 5 > 0:
#                 if arr[i][j][3] == 2:
#                     for direction in range(1, 8, 2):
#                         fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], direction))
#                 else:
#                     for direction in range(0, 7, 2):
#                         fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], direction))
#             elif arr[i][j][2] == 1:
#                 fireballs.append((i, j, arr[i][j][0], arr[i][j][1], arr[i][j][3]))
#     # print(*arr, sep='\n')
#     # print('==================')
# # arr = [[[0, 0, 0, -1] for _ in range(n)] for _ in range(n)]  # 질량합, 속력합, 파이어볼수, 짝수0 홀수1 섞이면2
# # for _ in range(len(fireballs)):
# #     move(*fireballs.pop())
# # print(fireballs)
# answer = 0
# for i in range(len(fireballs)):
#     answer += fireballs[i][2]
# # # for i in range(n):
# # #     for j in range(n):
# # #         answer += arr[i][j][0]
# print(answer)

