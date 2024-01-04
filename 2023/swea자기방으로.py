# def find_num(x, y):
#     if x < y:
#         if x % 2:
#             if y % 2:
#                 return x, y + 1
#             else:
#                 return x, y
#         else:
#             if y % 2:
#                 return x - 1, y + 1
#             else:
#                 return x - 1, y
#     else:
#         if y % 2:
#             if x % 2:
#                 return y, x + 1
#             else:
#                 return y, x
#         else:
#             if x % 2:
#                 return y - 1, x + 1
#             else:
#                 return y - 1, x
#
#
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     students = [sorted(find_num(*list(map(int, input().split())))) for _ in range(n)]
#
#     visited = [0] * n
#     answer = 0
#     students.sort()
#     for j in range(n):
#         if visited[j]:
#             continue
#         visited[j] = 1
#         answer += 1
#         right = students[j][1]
#         for i in range(j + 1, n):
#              if visited[i]:  # 여기 방문 체크를 안 했네~
#                 continue
#             if students[i][0] > right:
#                 visited[i] = 1
#                 right = students[i][1]
#     print(f'#{tc} {answer}')

for tc in range(1, int(input()) + 1):
    n = int(input())
    students = list(tuple(map(int, input().split())) for _ in range(n))
    visited = [0] * 200
    for i in range(n):
        left, right = (students[i][0] - 1) // 2, (students[i][1] - 1) // 2
        start = min(left, right)
        visited[start] += 1
        for j in range(1, abs(left - right) + 1):  # range(0)일 때 주의
            visited[start + j] += 1

    print(f'#{tc} {max(visited)}')
