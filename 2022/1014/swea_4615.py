import copy
# 원래 배열과, deepcopy한 배열을 들고있다
# (for문) 여덟 방향을 다 볼건데
# (while문) 다른색 돌이면 copy 배열에서 색을 바꾸면서 전진
# 다른 돌이다가 나랑 같은 돌이면 찐 배열에 저장하고, 아니면 그냥 버리기
def osello(r, c, color, board):
    board[r][c] = color  # 플레이어가 놓은 돌을 먼저 arr에 올려주고 주변 탐색
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        adj = copy.deepcopy(board)
        nr = r + dr
        nc = c + dc
        while 0 <= nr < n and 0 <= nc < n and adj[nr][nc] and adj[nr][nc] != color:
            adj[nr][nc] = color
            nr += dr
            nc += dc
            if 0 <= nr < n and 0 <= nc < n and adj[nr][nc] and adj[nr][nc] == color:
                board = adj
    else:
        return board


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    # [0] 시작 배열 만들기
    arr = [[0] * n for _ in range(n)]
    arr[n//2][n//2] = arr[n//2-1][n//2-1] = 2
    arr[n//2][n//2-1] = arr[n//2-1][n//2] = 1

    # [1] 돌을 놓으면 함수로 바뀐 arr을 뱉는다.
    for _ in range(m):
        x, y, c = map(int, input().split()) # 흑=1 백=2
        arr = osello(y-1, x-1, c, arr)

    # [2] 돌 세기
    black = 0
    white = 0
    for line in arr:
        black += line.count(1)
        white += line.count(2)

    print(f'#{tc} {black} {white}')