'''
for i for j 를 보면서 이동시킬거면 바로 이동시키면 안 되지, 이동한 애를 다시 이동시키니까
'''
from collections import deque


def move(man, x, y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = (x, y)
    q = deque([(x, y)])
    while q:
        cr, cc = q.popleft()
        for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc][0] == 0:
                q.append((nr, nc))
                visited[nr][nc] = (cr, cc)
                if (nr, nc) == goals[man]:

                    # print(man, '목적지찾음')
                    # print(*visited, sep='\n')
                    r, c = nr, nc
                    while visited[r][c] != (x, y):
                        r, c = visited[r][c]
                    return r, c
        # print(man, 'visited')
        # print(*visited, sep='\n')


def find(man):
    q = deque([goals[man]])
    visited = [[0] * N for _ in range(N)]
    visited[q[0][0]][q[0][1]] = 1
    candidate = []
    while q and not candidate:
        for day in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc][0] == 0:
                    if basecamp[nr][nc] == 1:
                        candidate.append((nr, nc))
                        visited[nr][nc] = 1
                    else:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
    candidate.sort()
    return candidate[0]


N, M = map(int, input().split())
basecamp = [list(map(int, input().split())) for _ in range(N)]
arr = [[[0] for _ in range(N)] for _ in range(N)]
goals = {}
info = {}
for idx in range(1, 1 + M):
    goals[idx] = tuple(map(lambda x: int(x) - 1, input().split()))

alive = [1] * (M + 1)
alive[0] = 0
answer = 1
while True:
    # [1] 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
    walls = []
    go = []
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 1:
                for p in range(len(arr[i][j]) - 1):
                    player = arr[i][j].pop()
                    pr, pc = move(player, i, j)
                    # 만약 편의점에 도착한다면
                    if (pr, pc) == goals[player]:
                        # 한 턴 뒤엔 벽으로 변경
                        walls.append((pr, pc))
                        alive[player] = 0
                    else:
                        # 아니면 arr에 추가해줘야함
                        go.append((pr, pc, player))
    for wr, wc in walls:
        arr[wr][wc][0] = 1
    for pr, pc, p in go:
        arr[pr][pc].append(p)
    # [2] t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
    if answer <= M:
        gr, gc = find(answer)
        arr[gr][gc].append(answer)
        arr[gr][gc][0] = 1
    # print(answer, '번 사람 들어감')
    # print(*arr, sep='\n')
    if not sum(alive):
        break
    answer += 1

print(answer)