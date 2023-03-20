# 11779 최소 비용 구하기
import heapq

def dij(start):
    global visited
    dist[start][0] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, node = heapq.heappop(q)
        if dist[node][0] < d:
            continue
        for next_d, next_node in arr[node]:
            cost = dist[node][0] + next_d
            if cost < dist[next_node][0]:
                dist[next_node][0] = cost
                dist[next_node][1] = dist[node][1] + [next_node]
                heapq.heappush(q, (cost, next_node))
            # elif cost == dist[next_node][0] and sum(dist[next_node][1]) > sum(dist[node][1] + [next_node]):
            #     dist[next_node][1] = dist[node][1] + [next_node]


n = int(input())  # 노드의 수
m = int(input())  # 간선의 수
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))
start, end = map(int, input().split())
dist = [[987654321, [start]] for _ in range(n + 1)]
dij(start)
visited = dist[end][1]
print(dist[end][0])
print(len(visited))
print(*visited)