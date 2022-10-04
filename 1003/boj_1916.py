# 백준 1916 최소비용 구하기
# import heapq
# import sys
# input = sys.stdin.readline
#
#
# def dij(start, end):
#     q = [(0, start)]
#     visited = set()
#     while q:
#         now, node = heapq.heappop(q)
#         if node not in visited:
#             dist[node] = min(now, dist[node])
#             visited.add(node)
#             if end in visited:
#                 return
#             for weight, next in adj[node]:
#                 if next not in visited and dist[next] > now + weight:
#                     heapq.heappush(q, (now + weight, next))
#
#
# n = int(input())  # 도시 수
# m = int(input())  # 버스 수
# adj = [[] for _ in range(n + 1)]
# for _ in range(m):
#     s, e, w = map(int, input().split())
#     adj[s].append((w, e))
# start, end = map(int, input().split())
# dist = [987654321] * (n + 1)  # 형식
# dist[start] = 0
# dij(start, end)
# print(dist[end])

from heapq import heappop, heappush
n = int(input())  # 도시 수
m = int(input())  # 버스 수
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
start, end = map(int, input().split())
dist = [987654321] * (n + 1)  # 형식
dist[start] = 0


def dij(start):
    q = [(0, start)]
    while q:
        now, node = heappop(q)
        if node == end:
            return
        if dist[node] < now:
            continue
        for weight, next in adj[node]:
            cost = dist[node] + weight
            if cost < dist[next]:
                dist[next] = cost
                heappush(q, (dist[next], next))

dij(start)
print(dist[end])

# import heapq
#
#
# def dij(start):
#     q = [(0, start)]
#     visited = set()
#     while q:
#         now, node = heapq.heappop(q)
#         if node not in visited:
#             dist[node] = now
#             visited.add(node)
#
#             for weight, next in adj[node]:
#                 cost = dist[node] + weight
#                 if next not in visited and cost < dist[next]:
#                     heapq.heappush(q, (cost, next))
#
#
# n = int(input())  # 도시 수
# m = int(input())  # 버스 수
# adj = [[] for _ in range(n + 1)]
# # 인접 그래프 받기
# for _ in range(m):
#     s, e, w = map(int, input().split())
#     adj[s].append((w, e))
# # 시작과 끝 노드
# start, end = map(int, input().split())
# # 최소 거리 리스트
# dist = [987654321] * (n + 1)  # 형식
# dist[start] = 0
#
# dij(start)
# print(dist[end])