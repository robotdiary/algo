# # 4881. 배열 최소 합 (D2)

# 파라미터 안 들고 가기
# def perm(depth):
#     global min_sum
#     if depth == n and sum(selection) < min_sum:
#         min_sum = sum(selection)
#         return
#     for i in range(n):
#         if not check[i]:
#             check[i] = 1
#             selection[depth] = arr[depth][i]
#             if sum(selection[0:depth+1]) >= min_sum:
#                 check[i] = 0 # 밑에로 안 가고 다시 시작할 거니까 여기도 써줘야 함
#                 continue
#             perm(depth + 1)
#             check[i] = 0
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     check = [0] * n
#     selection = [0] * n
#     min_sum = 10000
#     perm(0)
#     print(f'#{tc} {min_sum}')
#
#
# 파라미터로 들고 가기
def perm(depth, acc):
    global min_num
    if acc > min_num:
        return
    if depth == n:
        if min_num > acc: # 조건 걸어주고
            min_num = acc
            return # 리턴
    for i in range(n):
        if not check[i]:
            check[i] = 1
            perm(depth + 1, acc + arr[depth][i])
            check[i] = 0
    return min_num


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    check = [0] * n
    min_num = 99999
    print(f'#{tc} {perm(0, 0)}')