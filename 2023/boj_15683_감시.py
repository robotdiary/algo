direction = {1: [[(0, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
             2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
             3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
             4: [[(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)]],
             5: [[(0, 1), (1, 0), (-1, 0), (0, -1)]]
             }
type = [0, 4, 2, 4, 4, 1]

n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]  # 문자열
cctvs = []
cnt = 0  # 빈 방 수
for i in range(n):
    for j in range(m):
        if arr[i][j] not in {'6', '0'}:
            cctvs.append((i, j, int(arr[i][j])))
        elif arr[i][j] == '0':
            cnt += 1
answer = 99999


def 감시(depth, acc, visited):  # cctv인덱스, 감시하는 방
    global answer
    if acc <= 0:
        answer = 0
        return
    if depth == len(cctvs):
        answer = min(answer, acc)
        return
    for k in range(type[cctvs[depth][2]]):
        stack = [(cctvs[depth][0], cctvs[depth][1])]
        visit = {(cctvs[depth][0], cctvs[depth][1])}
        sm = 0
        while stack:
            cr, cc = stack.pop()
            for dr, dc in direction[cctvs[depth][2]][k]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visit and (nr, nc) not in visited and arr[nr][nc] != '6':
                    stack.append((nr, nc))
                    visit.add((nr, nc))
                    if arr[nr][nc] == '0':
                        sm += 1
        print('============')
        print(depth, cctvs[depth], sm, acc-sm)
        print('진행방향', direction[cctvs[depth][2]][k])
        print('visit', visit)
        감시(depth + 1, acc - sm, visited.union(visit))
        if not answer:
            return


감시(0, cnt, set())
print(answer)
