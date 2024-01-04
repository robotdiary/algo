import heapq


def dijkstra(start):
    distance = [987654321] * (N + 1)
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in adj[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance


N, E = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [[0] * (N+1) for _ in range(N+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))
v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1_path, v2_path)
print(result if result < 987654321 else -1)
