# dfs와 bfs
from collections import deque


def dfs(start):
    stack = [start]
    visited = []
    while stack:
        target = stack.pop()
        if target not in visited:
            visited.append(target)
            next = sorted(arr[target], reverse=True)
            for ni in next:
                stack.append(ni)
    return visited


def bfs(start):
    q = deque([start])
    visited = []
    while q:
        target = q.popleft()
        if target not in visited:
            visited.append(target)
            next = sorted(arr[target])
            for ni in next:
                q.append(ni)
    return visited


n, m, v = map(int, input().split())  # 정점, 간선, 시작정점
arr = [[] for _ in range(n + 1)]
for i in range(m):
    s, e = map(int, input().split())
    arr[e].append(s)
    arr[s].append(e)

print(*dfs(v))
print(*bfs(v))
