from collections import deque


def solve():
    global answer
    service = arr[i][j]
    수익 = -운영비용 + (service * M)
    size = 운영비용 - 1

    q = deque([(i, j)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    time = 1
    if K == 3 and i == 3 and j == 3:
        pass
    while q and time < K:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    if arr[nr][nc] == 1:
                        service += 1
                        수익 += M
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    size -= 1
                    if 수익 + (size * M) < 0:
                        return
        else:
            time += 1
    # print(K, '크기 순회')
    # print(*visited, sep='\n')

    if 수익 >= 0:
        answer = max(answer, service)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [0] 총 집의 수 세기
    rooms = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                rooms += 1

    mx = M * rooms  # 최대 수익
    K = 2  # 서비스 크기
    answer = 1 if rooms else 0
    while True:
        운영비용 = K * K + (K - 1) * (K - 1)
        if 운영비용 > mx:
            break

        for i in range(N):
            for j in range(N):
                solve()
        K += 1

    print(f'#{tc} {answer}')