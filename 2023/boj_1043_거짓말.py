from collections import deque
N, M = map(int, input().split())  # 사람수 파티수
stack = deque(map(int, input().split()))
stack.popleft()

mans = {i: [] for i in range(1, N + 1)}
parties = {i: [] for i in range(M)}
for idx in range(M):
    b = list(map(int, input().split()))
    for man in range(1, 1 + b[0]):
        mans[b[man]].append(idx)
        parties[idx].append(b[man])

alive = [1] * M
visited = [0] * (N + 1)
while stack:
    current = stack.pop()
    if visited[current]:
        continue
    for party in mans[current]:
        if alive[party]:
            alive[party] = 0
            stack += parties[party]
print(sum(alive))

"""
사람딕트 = {사람 : [가는 파티]}
파티딕트 = {파티 : [오는 사람]}
진실을 아는 사람 stack = []
stack을 돌면서
방문했던 사람이 아니면
그 자가 방문하는 모든 파티 돌면서
if alive:
    alive = 0
    그 파티 사람들 모두 stack에 추가
"""