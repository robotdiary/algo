import heapq

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
sr, sc, sd = map(lambda x: int(x) - 1, input().split())
gr, gc, gd = map(lambda x: int(x) - 1, input().split())

direction = {0: 0, 1: 2, 2: 1, 3: 3}  # 인풋방향 : di dj 인덱스
di = [0, 1, 0, -1]  # 동, 남, 서, 북
dj = [1, 0, -1, 0]
q = [(0, sr, sc, direction[sd])]  # 명령횟수, 현재 위치, 방향
visited = set()
while q:
    acc, cr, cc, d = heapq.heappop(q)
    if (cr, cc, d) == (gr, gc, direction[gd]):
        print(acc)
        break
    elif (cr, cc) == (gr, gc):
        heapq.heappush(q, (acc + 1, cr, cc, (d + 1) % 4))
        heapq.heappush(q, (acc + 2, cr, cc, (d + 2) % 4))
        heapq.heappush(q, (acc + 1, cr, cc, (d + 3) % 4))
        continue
    if (cr, cc) not in visited:
        visited.add((cr, cc))
        for i in range(4):
            nd = (d + i) % 4
            for k in range(1, 4):
                nr, nc = cr + (di[nd] * k), cc + (dj[nd] * k)
                if 0 <= nr < m and 0 <= nc < n and not arr[nr][nc] and (nr, nc) not in visited:
                    # d % 4로 계산해서 집어넣기
                    # i == 3 은 1로
                    heapq.heappush(q, (acc + 1 + (1 if i == 3 else i), nr, nc, nd))
                else:
                    break