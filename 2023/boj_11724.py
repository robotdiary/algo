n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

answer = 0
for i in range(n+1):
    if not visited[i]:
        stack = [i]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = 1
            stack += adj[node]
        else:
            answer += 1
print(answer - 1)

# 연결 요소의 개수
# def find_parent(x):
#     if parent[x] == x:
#         return x
#     else:
#         return find_parent(parent[x])
#
#
# n, m = map(int, input().split())  # 정점의 개수, 간선의 개수
# parent = list(range(n + 1))
# adj = [[] for _ in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     adj[u] = v
#     adj[v] = u
# for j in range(n):
#     find_parent(j)
#     print(parent)
# print(len(set(parent)) - 1)