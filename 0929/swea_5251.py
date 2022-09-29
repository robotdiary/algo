# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리 D4
from heapq import heappush, heappop


def dij(start):
    distance = [inf] * (v + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue
        for i in adj[node]:
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance[n]


for tc in range(1, int(input()) + 1):
    n, e = map(int, input().split())  # 노드, 간선
    v = n + 1
    inf = 987654321
    adj = [[] for _ in range(v)]
    for _ in range(e):
        start, end, w = map(int, input().split())
        adj[start].append((end, w))

    print(f'#{tc} {dij(0)}')
