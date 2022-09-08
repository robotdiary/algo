# # 4615. 재미있는 오셀로 게임 D3
# def osello(dr, dc, color):
#     stack = []
#     visited = []
#     answer = []
#     # [1] 여덟 방향을 돌면서 이웃한 다른 색 돌을 찾는다.
#     for search in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
#         if 0 < dr+search[0] < n+1 and 0 < dc+search[1] < n+1 and arr[dr+search[0]][dc+search[1]] != 0 and arr[dr+search[0]][dc+search[1]] != color:
#             stack.append(search) # search는 방향
#     # [2] 이웃한 돌 방향으로 계속 나아가면서 탐색
#     while stack:
#         now = stack.pop() # 나아갈 방향
#         nr = dr
#         nc = dc
#         while 0 < nr+now[0] < n+1 and 0 < nc+now[1] < n+1:
#             nr += now[0]
#             nc += now[1]
#             # 다른 색이면 visited에 추가
#             if arr[nr][nc] and arr[nr][nc] != color:
#                 visited.append((nr, nc))
#             # 같은 색이 나오면 멈추고 visited를 색 바꿀 리스트에 추가하고 초기화
#             elif arr[nr][nc] == color:
#                 answer = answer+visited
#                 visited = []
#                 break
#     # [3] 전진이 끝날 때까지 다른색이 안 나오면 visited를 다 지움
#         else:
#             visited = []
#
#     # 색 바꿀 리스트의 모든 좌표의 색 바꾸기
#     for t_r, t_c in answer:
#         arr[t_r][t_c] = color
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

drc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]                            # 8방 탐색

def reverse_stone(col, row, stone):                                                                     # 돌 놓은 곳 8방 탐색하여 뒤집기 기능하는 함수
    pass
    num = 2                                                                                             # num = 현재 색깔 돌의, 반대 색깔 돌

    if stone == 2:
        num = 1

    # 8방향 탐색
    for direction in range(8):
        r_position = row + drc[direction][0]
        c_position = col + drc[direction][1]

        cnt = 1                                                                                         # 특정방향으로 몇번 이동 가능한지
        while 1 <= r_position <= N and 1 <= c_position <= N and board[r_position][c_position] == num:   # 인덱스 범위 이내 & 반대 색깔 돌일 경우, 해당 방향으로 계속 진행
            r_position += drc[direction][0]
            c_position += drc[direction][1]

            if board[r_position][c_position] == num:                                                    # 이동한 곳이 반대 색깔 돌일 경우, cnt +1 증가
                cnt += 1

        if 1 <= r_position <= N and 1 <= c_position <= N and board[r_position][c_position] == stone:    # 마지막으로 이동한 곳이, 범위 이내이고, 같은 색깔의 돌일 경우
            for i in range(1, cnt+1):                                                                   # 그 사이에 있는 돌들 뒤집어주기
                r_position = row + drc[direction][0] * i
                c_position = col + drc[direction][1] * i

                board[r_position][c_position] = stone


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * (N+2) for _ in range(N+2)]       # index control위해 N+2 개씩으로 하였음

    start = N // 2
    # 흑돌 찍기
    board[start][start] = 2
    board[start+1][start+1] = 2
    # 백돌 찍기
    board[start + 1][start] = 1
    board[start][start + 1] = 1
    # print(board)

    # M회 돌 놓기 실행
    for _ in range(M):
        col, row, stone = map(int, input().split())
        # 해당 위치에 돌 놓기
        board[row][col] = stone
        # 주변 돌들 뒤집기
        reverse_stone(col, row, stone)

    # 최종 오셀로 판 상황확인하여 백돌, 흑돌 개수 구하기
    B_cnt = 0
    W_cnt = 0
    for i in range(N+2):
        for j in range(N+2):
            if board[i][j] == 1:
                B_cnt += 1
            elif board[i][j] == 2:
                W_cnt += 1

    print(f'#{tc} {B_cnt} {W_cnt}')