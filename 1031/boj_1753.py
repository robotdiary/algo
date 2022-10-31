# boj 1753 최단경로
import heapq


def dij(start):
    dist = [987654321] * (v + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        w, n = heapq.heappop(q)
        if dist[n] < w:  #
            continue
        for next in range(v+1):
            cost = dist[n] + graph[n][next]
            if cost < dist[next]:
                dist[next] = cost
    return dist


v, e = map(int, input().split())
start_node = int(input())
graph = [[987654321] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    s, e, weight = map(int, input().split())
    graph[s][e] = weight
print(dij(start_node))
for i in dij(start_node)[1:]:
    if i == 987654321:
        print('INF')
    else:
        print(i)