# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
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
        for i in [arr[node[0]][node[1]], (node[0], node[1])]:  # 거리, 노드 번호
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance[n]


for tc in range(1, int(input()) + 1):
    n, e = int(input())  # 가로세로
    v = n ** 2
    inf = 987654321
    arr = [list(map(int, input().split())) for _ in range(n)]

        # start, end, w = map(int, input().split())
        # adj[start].append((end, w))

    print(f'#{tc} {dij((0, 0))}')


