# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
from heapq import heappush, heappop

for tc in range(1, int(input()) + 1):
    n = int(input())  # 가로세로
    inf = 987654321
    arr = [list(map(int, input().split())) for _ in range(n)]
    adj = [[inf]*n for _ in range(n)]
    adj[0][0] = 0  # 집은 돈 안 듬

    q = [(adj[0][0], 0, 0)]
    while q:
        dist, nr, nc = heappop(q)
        if adj[nr][nc] < dist:  # ?
            continue
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 거리, 노드 번호
            if 0 <= nr+dr < n and 0 <= nc+dc < n and arr[nr+dr][nc+dc] <= arr[nr][nc]:
                cost = adj[nr][nc] + 1
                if cost < adj[nr+dr][nc+dc]:
                    adj[nr+dr][nc+dc] = cost
                    heappush(q, (adj[nr+dr][nc+dc], nr+dr, nc+dc))
            elif 0 <= nr+dr < n and 0 <= nc+dc < n:
                cost = adj[nr][nc] + 1 + (arr[nr + dr][nc + dc] - arr[nr][nc])
                high = arr[nr + dr][nc + dc]
                if cost < adj[nr + dr][nc + dc]:
                    adj[nr + dr][nc + dc] = cost
                    heappush(q, (adj[nr + dr][nc + dc], nr + dr, nc + dc))
            # print(adj)
    print(f'#{tc} {adj[n-1][n-1]}')


