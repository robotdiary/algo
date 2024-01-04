# # 러시아 국기 같은 기발
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     arr = [list(input()) for _ in range(n)]
#
#     counts = [[0]*m for _ in range(n)]  # 칠해진 색이 몇 갠지 미리 세고 그 숫자의 합으로 확인하는 방법
#     answer = 999999999
#     # 줄 당 무슨 색인지 체크하는 부분
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 'W':
#                 counts[0][i] += 1
#             elif arr[i][j] == 'B':
#                 counts[1][i] += 1
#             else:
#                 counts[2][i] += 1
#     # 각 색을 칠해야하는 수
#     acc = [0, 0, 0]
#     for i in range(n-2):
#         acc[0] += m - counts[0][i]
#         for j in range(i+1, n-1):
#             acc[1] += m - counts[1][j]
#             if sum(acc) >= answer:  # 이미 답보다 커졌다면 멈춰!
#                     acc[1] = 0
#                     break
#             for k in range(j+1, n):
#                 acc[2] += m - counts[2][k]
#                 if sum(acc) >= answer:  # 이미 답보다 커졌다면 멈춰!
#                     acc[2] = 0
#                     break
#             else:
#                 answer = sum(acc)
#             acc[2] = 0  # 앞의 색부터 다시 확인할 거니까 뒤는 0으로 초기화
#         acc[1] = 0
#     print(f'#{tc} {answer}')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    answer = 987654321

    for i in range(1, n):
        for j in range(i + 1, n):
            check = 0
            for k in range(n):
                if k < i:
                    check += len(arr[k]) - arr[k].count('W')
                elif k < j:
                    check += len(arr[k]) - arr[k].count('B')
                else:
                    check += len(arr[k]) - arr[k].count('R')
            answer = min(answer, check)

    print(f'#{tc} {answer}')