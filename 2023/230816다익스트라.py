import heapq


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    parent[find_parent(y)] = find_parent(x)


V, E = map(int, input().split())
parent = list(range(V + 1))
q = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    heapq.heappush(q, (weight, start, end))

acc = 0
cnt = 0
while q and cnt < V:
    w, s, e = heapq.heappop(q)
    if find_parent(s) != find_parent(e):
        acc += w
        union(s, e)
        cnt += 1

print(acc)