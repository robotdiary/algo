# 그래프 연습문제 2
from collections import deque
info = list(map(int, input().split()))
v = 0
for i in info:
    if i > v:
        v = i
arr = [[0] * (v + 1) for _ in range(v + 1)]
for node in range(0, len(info), 2):
    arr[info[node]][info[node+1]] = 1
Q = deque([1])
visited = []
while Q:
    current = Q.popleft()
    if current not in visited:
        visited.append(current)
    for i in range(v + 1):
        if arr[current][i] and i not in visited:
            Q.append(i)
print(*visited)
