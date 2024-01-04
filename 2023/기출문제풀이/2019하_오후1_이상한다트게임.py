N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = N * M

for tc in range(Q):
    if not cnt:
        break
    # [1] 회전 요청
    X, D, K = map(int, input().split())
    for i in range(1, N + 1):
        if not i % X:
            if D:  # 반시계
                arr[i-1] = arr[i-1][(K % M):] + arr[i-1][:(K % M)]
            else:
                arr[i-1] = arr[i-1][(-K % M):] + arr[i-1][:(-K % M)]
    # print('돌림')
    # print(*arr, sep='\n')
    # [2] 인접한 같은 수 지우기
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 0:
                dead = 0
                target = arr[i][j]
                stack = [(i, j)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        nc %= M
                        if 0 <= nr < N and arr[nr][nc] == target:
                            stack.append((nr, nc))
                            arr[nr][nc] = -1
                            dead += 1
                            flag = 1
                if dead:
                    arr[i][j] = -1
                    cnt -= dead + 1
                    # print('지움', target)
                    # print(*arr, sep='\n')
    if not flag:
        # 정규화
        개수 = 0
        합 = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] >= 0:
                    개수 += 1
                    합 += arr[i][j]
        if 개수:
            average = 합 / 개수
            # print(개수, 합, average)
            for i in range(N):
                for j in range(M):
                    if arr[i][j] >= 0:
                        if arr[i][j] > average:
                            arr[i][j] -= 1
                        elif arr[i][j] < average:
                            arr[i][j] += 1
        # print('정규화')
        # print(*arr, sep='\n')
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            answer += arr[i][j]
print(answer)