# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D4
# [2] MST - Prim
def prim():
    distance = [inf] * (v + 1)  # 큰 수로 초기화
    visited = [0] * (v + 1)
    distance[v] = 0  # 아무데서나 시작해도 똑같음, v에서 시작

    for _ in range(v + 1):
        idx = -1
        value = inf
        for i in range(v + 1):
            if not visited[i] and distance[i] < value:
                value = distance[i]
                idx = i
        visited[idx] = 1
        for i in range(v + 1):
            if not visited[i] and arr[idx][i] < distance[i]:
                distance[i] = arr[idx][i]
    return sum(distance)


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    inf = 987654321
    arr = [[inf]*(v+1) for _ in range(v + 1)]
    for _ in range(e):
        start, end, w = map(int, input().split())
        arr[start][end] = arr[end][start] = w
    print(f'{tc} {prim()}')

# [1] MST - Kruskal
# def find_set(node):
#     # path compression
#     if parent[node] != node:
#         parent[node] = find_set(parent[node])
#     return parent[node]
#
#
# def union(node1, node2):
#     node1 = find_set(node1)
#     node2 = find_set(node2)
#     if rank[node1] > rank[node2]:
#         parent[node2] = node1
#     elif rank[node1] < rank[node2]:
#         parent[node1] = node2
#     else:
#         parent[node2] = node1
#         rank[node1] += 1
#
#
# for tc in range(1, int(input()) + 1):
#     v, e = map(int, input().split())  # 0 ~ v노드, 간선 수
#     edges = []
#     for _ in range(e):
#         start, end, w = map(int, input().split())
#         edges.append((w, start, end))
#
#     edges.sort()  # 가중치 작은것부터 확인하도록 정렬
#                   # edges.sort(key=lambda x: x[2])
#     # [1] make_set : 부모 리스트, 노드 자신으로 초기화
#     parent = [i for i in range(v + 2)]  # list(range(v + 2))
#     rank = [0] * (v + 2)
#     answer = 0
#     for w, start, end in edges:
#         if find_set(start) != find_set(end):
#             union(start, end)
#             answer += w
#     print(f'#{tc} {answer}')
'''
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
[0, 1, 2, 3, 4, 5]
[0, 0, 0, 0, 0, 0]
0
[0, 1, 2, 3, 2, 5]
[0, 0, 1, 0, 0, 0]
1
[0, 2, 2, 3, 2, 5]
[0, 0, 2, 0, 0, 0] [0, 0, 1, 0, 0, 0]
3
[2, 2, 2, 3, 2, 5]
[0, 0, 3, 0, 0, 0] [0, 0, 1, 0, 0, 0]
6
[2, 2, 2, 2, 2, 5]
[0, 0, 4, 0, 0, 0] [0, 0, 1, 0, 0, 0]
13
[2, 2, 2, 2, 2, 5]
[0, 0, 4, 0, 0, 0] [0, 0, 1, 0, 0, 0]
13
[2, 2, 2, 2, 2, 5]
[0, 0, 4, 0, 0, 0] [0, 0, 1, 0, 0, 0]
13
#2 13
'''