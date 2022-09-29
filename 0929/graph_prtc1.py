# 그래프 연습문제 1
v = 7
info = list(map(int, input().split()))
edges = list([] for i in range(v + 1))
for i in range(len(info)//2):  # 0, 1, 2 ~ 7
    edges[info[i * 2]].append(info[i * 2 + 1])  # 0, 2, 4 ~ 14
    edges[info[i * 2 + 1]].append(info[i * 2])
stack = [1]
visited = []
while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    for edge in edges[current]:
        if edge not in visited:
            stack.append(edge)
print(*visited)