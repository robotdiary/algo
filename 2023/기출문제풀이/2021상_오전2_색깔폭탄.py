'''
0번 블럭을 다른 애가 공유할 수 있는데
visited를 찍어버려서 그룹을 덜 만들게 된다!!
방문 체크
'''
def find():
    global answer
    visited = [[0] * N for _ in range(N)]
    mx = ()
    for i in range(N-1, -1, -1):
        for j in range(N):
            if visited[i][j] == 0 and 1 <= arr[i][j]:
                idx = 0
                q = [(i, j)]
                visited[i][j] = 1
                red = 0
                while idx < len(q):
                    cr, cc = q[idx]
                    if (cr, cc ) == (4, 3):
                        pass
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                            if arr[nr][nc] == arr[i][j]:
                                q.append((nr, nc))
                                visited[nr][nc] = 1
                            elif arr[nr][nc] == 0 and (nr, nc) not in q:
                                q.append((nr, nc))
                                red += 1
                    idx += 1
                if len(q) >= 2:
                    mx = max(mx, (len(q), -red, i, -j, q))
    print(mx)
    if mx:
        answer += (mx[0] ** 2)
        for r, c in mx[4]:
            arr[r][c] = -2
        return True
    return False


def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if 0 <= arr[i][j] <= M:
                cr, cc = i, j
                while cr < N-1 and arr[cr+1][cc] == -2:
                    arr[cr+1][cc], arr[cr][cc] = arr[cr][cc], arr[cr+1][cc]
                    cr += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# -1검 0빨 1-m
answer = 0
while True:
    # [1] 현재 격자에서 크기가 가장 큰 폭탄 묶음을 찾습니다.
    # 2개 이상의 폭탄 / 모두 같은 색깔 | 빨간색 폭탄을 포함 / 빨강만 X / 인접
    # 개수, 적은빨강, 큰행, 작은열
    # 폭탄 묶음이 존재하지 않을 때 끝
    # [2] 폭탄들을 전부 제거 점수+ (개수*개수)
    if not find():
        break
    print('제거')
    print(*arr, sep='\n')
    # [3] 중력 (검은돌 제외)
    gravity()
    print('중중력')
    print(*arr, sep='\n')
    # [4] 반시계 방향으로 90'
    arr = [[arr[i][N-1-j] for i in range(N)] for j in range(N)]
    print('반시계')
    print(*arr, sep='\n')
    # [5] 중력
    gravity()
    print('중중력')
    print(*arr, sep='\n')
    # break
print(answer)

# arr = [[1, 2], [3, 4]]
# arr = [[arr[i][2 - 1 - j] for i in range(2)] for j in range(2)]
# print(*arr, sep='\n')