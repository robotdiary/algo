'''
3시 - 3시 25분 (구현 10분 / 왜틀렸지 15분) 좌회전인데 왜 우회전 하고있냐
'''


def solve(cr, cc, d):
    visited = [[0] * M for _ in range(N)]
    visited[cr][cc] = 1
    while True:
        # [1] 좌회전 후 전진
        for nd in range(4):
            d = (d - 1) % 4  # 좌회전인데 왜 우회전 하고있냐... 에휴
            # 미방문 차도면 전진
            nr, nc = cr + di[d], cc + dj[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == '0':
                visited[nr][nc] = visited[cr][cc] + 1
                cr, cc = nr, nc
                break
        # [2] 전진 못하면 후진
        else:
            nr, nc = cr + di[oppo[d]], cc + dj[oppo[d]]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0':
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                else:
                    visited[nr][nc] = visited[cr][cc]
                cr, cc = nr, nc
            # [3] 후진 못하면 중지
            else:
                return visited[cr][cc]


N, M = map(int, input().split())
X, Y, D = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)
oppo = {0: 2, 2: 0, 1: 3, 3: 1}
print(solve(X, Y, D))
