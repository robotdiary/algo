# 체스판 다시 칠하기
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
w_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
b_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
answer = 987654321
# [1] 체스판의 시작점 정하기
for i in range(0, N - 7):
    for j in range(0, M - 7):
        # 두 가지 체스판 확인
        for board in range(2):
            brr = w_board
            if board == 1:
                brr = b_board
            # [2] 바꿔야 하는 개수 확인
            ans = 0
            for r in range(8):
                for c in range(8):
                    if arr[i+r][j+c] != brr[r][c]:
                        ans += 1
                    if ans >= answer:  # 백트래킹
                        break
                if ans >= answer:
                    break
            if ans < answer:
                answer = ans
print(answer)