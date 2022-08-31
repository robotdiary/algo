# 9489 고대유적 (D2)
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # [1] 가로 확인
    for i in range(n):
        length1 = 0 # 줄이 바뀔때마다 초기화
        for j in range(m):
            if arr[i][j]:
                length1 += 1
                if length1 > answer:
                    answer = length1
            else: # 0이 나오면 길이 초기화
                length1 = 0
    # [2] 세로 확인
    for i in range(m):
        length2 = 0 # 줄이 바뀔 때마다 초기화
        for j in range(n):
            if arr[j][i]:
                length2 += 1
                if length2 > answer:
                    answer = length2
            else: # 0이 나오면 초기화
                length2 = 0

    print(f'#{tc} {answer}')

# runtime error
# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     answer = 0
#     for i in range(n):
#         length1 = 0
#         length2 = 0
#         for j in range(m):
#             if arr[i][j]:
#                 length1 += 1
#                 if length1 > answer:
#                     answer = length1
#             else:
#                 length1 = 0
#             if arr[j][i]:
#                 length2 += 1
#                 if length2 > answer:
#                     answer = length2
#             else:
#                 length2 = 0
#
#     print(f'#{tc} {answer}')