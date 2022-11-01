# BFS visited 탐색시 찍기 (더 빠름)
from collections import deque

for tc in range(1, int(input()) + 1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]

    # 시작점 넣어 놓고 0으로 바꾸기
    q = deque([(n // 2, n // 2)])
    answer = field[n // 2][n // 2]
    visited = {(n // 2, n // 2)}

    # 마름모를 만들 만큼 반복
    cnt = n // 2
    while cnt:
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited:
                    answer += field[cr + dr][cc + dc]
                    q.append((cr + dr, cc + dc))
                    visited.add((cr + dr, cc + dc))
        else:
            cnt -= 1
    print(f'#{tc} {answer}')

# BFS visited 먼저 찍기
# from collections import deque
#
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     field = [list(map(int, input())) for _ in range(n)]
#
#     # 시작점 넣어 놓고 0으로 바꾸기
#     q = deque([(n // 2, n // 2)])
#     answer = 0
#     visited = set()
#
#     # 마름모를 만들 만큼 반복
#     cnt = n // 2 + 1
#     while cnt:
#         for _ in range(len(q)):
#             cr, cc = q.popleft()
#             if (cr, cc) not in visited:
#                 visited.add((cr, cc))
#                 answer += field[cr][cc]
#                 for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                     if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited:
#                         q.append((cr + dr, cc + dc))
#         else:
#             cnt -= 1
#     print(f'#{tc} {answer}')

# 기본 코드
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     field = [list(map(int, input())) for _ in range(n)]
#     answer = 0
#     for i in range(n // 2 + 1):
#         if i == n // 2:
#             answer += sum(field[i])
#         else:
#             answer += sum(field[i][n // 2 - i:n // 2 + 1 + i])
#             answer += sum(field[n - 1 - i][n // 2 - i:n // 2 + 1 + i])
#
#     print(f'#{tc} {answer}')