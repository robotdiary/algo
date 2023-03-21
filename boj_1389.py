#케빈 베이컨의 6단계 법칙
from collections import deque
n, m = map(int, input().split())
adj = [set() for _ in range(n + 1)]
answer = [1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)
# for idx in range(n + 1):
#     adj[idx] = list(adj[idx])
# print(adj)
for i in range(1, n + 1):      # 본인
    for j in range(1, n + 1):  # 찾는 친구
        if j == i:
            continue
        q = deque()
        q.append(i)
        visited = {i}
        while q:
            for bfs in range(len(q)):
                node = q.popleft()
                if node not in visited:
                    visited.add(node)
                else:
                    continue
                if j not in adj[node]:
                    q += deque(adj[node])
                else:
                    q = 0
                    break
            else:
                answer[i] += 1
print(answer)

