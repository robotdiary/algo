v, e = map(int, input().split())
adj_matrix = [[0] * (v + 1) for _ in range(v+1)]
for _ in range(e):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1
q = [1]
visited = []

while q:
    current = q.pop(0)
    if current not in visited:
        visited.append(current)
    for destination in range(v + 1):
        if adj_matrix[current][destination] and destination not in visited:
            q.append(destination)
print('이동경로: ', *visited)