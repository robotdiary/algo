import sys; input = sys.stdin.readline


def dfs(i):
    node = 0
    dist = 0
    stack = [(0, i)]
    visited = [0] * (n+1)
    visited[i] = 1
    while stack:
        acc, current = stack.pop()
        for dest, weight in adj[current]:
            if visited[dest] == 1:
                continue
            if acc + weight > dist:
                dist = acc + weight
                node = dest
            visited[dest] = 1
            stack.append((acc + weight, dest))
    return node, dist  # 노드, 거리


INF = 987654321
n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

mx, _ = dfs(1)
_, answer = dfs(mx)
print(answer)
