# # 4615. 재미있는 오셀로 게임 D3
# def osello(dr, dc, color):
#     stack = []
#     visited = []
#     answer = []
#     # nr, nc = dr, dc # 현재 위치
#     for search in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # 여덟 방향을 돌면서 다른 색을 찾는다.
#         if 0 < dr+search[0] < n+1 and 0 < dc+search[1] < n+1 and arr[dr+search[0]][dc+search[1]] and arr[dr+search[0]][dc+search[1]] != color:   # 다른 색이 있으면 스택에 추가한다.
#             stack.append(search) # search는 방향
#     # print(stack) (1, 0)
#     # print('stack:', stack)
#     while stack: # 스택을 돌면서 선택
#         now = stack.pop() # 나아갈 방향
#         # nr = dr + now[0]
#         # nc = dc + now[1]
#         nr = dr
#         nc = dc
#         # visited.append((nr, nc))  # 방문에 넣고 [(1, 2), ]
#         # print('visited:', visited)
#         while 0 < nr+now[0] < n+1 and 0 < nc+now[1] < n+1: # 스택에서 전진하면서,
#             nr += now[0]
#             nc += now[1]
#             if arr[nr][nc] and arr[nr][nc] != color: # 다른색이면 방문에 추가
#                 visited.append((nr, nc))
#             elif arr[nr][nc] == color: # 같은 색이 나오면  멈춤
#                 answer = answer+visited
#                 visited = []
#                 break # 전진이 끝날 때까지 다른색이 안 나오면 스택을 다 지움
#         else:
#             visited = []
#     # visited의 모든 좌표의 색을 바꾸기
#     for t_r, t_c in answer:
#         arr[t_r][t_c] = color
#     # print('answer:', answer)
#     # print(arr)
#     return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split()) # 바둑판 배열, 놓는 횟수
#     arr = [[0] * (n+1) for _ in range(n+1)]
#     arr[n//2][n//2], arr[n//2][n//2+1], arr[n//2+1][n//2], arr[n//2+1][n//2+1] = 2, 1, 1, 2
#     for put in range(m):
#         c, r, color = map(int, input().split())
#         if color == 1:  # 흑돌
#             arr[r][c] = 1
#         else:           # 백돌
#             arr[r][c] = 2
#         # 놓은 돌의 가로 세로 대각선을 확인해서 거기 같은 게 있는지 확인
#         osello(r, c, color)
#
#     white = 0
#     black = 0
#     for i in range(n+1):
#         white += arr[i].count(2)
#         black += arr[i].count(1)
#
#     print(f'#{tc} {black} {white}')

def osello(dr, dc, color):
    stack = []

    answer = []
    # [1] 여덟 방향을 돌면서 이웃한 다른 색 돌을 찾는다.
    for search in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if 0 < dr+search[0] < n+1 and 0 < dc+search[1] < n+1:
            if arr[dr+search[0]][dc+search[1]] != 0 and arr[dr+search[0]][dc+search[1]] != color:
                stack.append(search) # search는 방향
    # [2] 이웃한 돌 방향으로 계속 나아가면서 탐색
    while stack:
        now = stack.pop() # 나아갈 방향
        nr = dr
        nc = dc
        while 0 < nr+now[0] < n+1 and 0 < nc+now[1] < n+1:
            nr += now[0]
            nc += now[1]
            visited = []
            # 다른 색이면 visited에 추가
            if arr[nr][nc] != 0 and arr[nr][nc] != color:
                visited.append((nr, nc))
            # 같은 색이 나오면 멈추고 visited를 색 바꿀 리스트에 추가하고 초기화
            elif arr[nr][nc] == color:
                for t_r, t_c in visited:
                    arr[t_r][t_c] = color
    #             answer = answer+visited
                break
            else:
                break
    # # [3] 전진이 끝날 때까지 다른색이 안 나오면 visited를 다 지움
    #     else:
    #         visited = []
        return

    # 색 바꿀 리스트의 모든 좌표의 색 바꾸기



T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split()) # 바둑판 배열, 놓는 횟수
    arr = [[0] * (n+1) for _ in range(n+1)]
    arr[n//2][n//2], arr[n//2][n//2+1], arr[n//2+1][n//2], arr[n//2+1][n//2+1] = 2, 1, 1, 2
    for put in range(m):
        c, r, color = map(int, input().split())
        if color == 1:  # 흑돌
            arr[r][c] = 1
        else:           # 백돌
            arr[r][c] = 2
        # 놓은 돌의 가로 세로 대각선을 확인해서 거기 같은 게 있는지 확인
        osello(r, c, color)

    white = 0
    black = 0
    for i in range(n+1):
        white += arr[i].count(2)
        black += arr[i].count(1)

    print(f'#{tc} {black} {white}')