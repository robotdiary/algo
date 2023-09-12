import heapq


def dfs(stack):
    while stack:
        cr, cc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = island
                stack.append((nr, nc))


def find_parent(x):
    if parent[x] == -1:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    parent[find_parent(b)] = find_parent(a)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
island = 2
edges = []
# 섬에 이름 짓기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = island
            dfs([(i, j)])
            island += 1

# 섬마다 연결선 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = i + dr, j + dc
                cnt = 0
                while 0 <= nr < n and 0 <= nc < m:
                    if arr[nr][nc] == arr[i][j]:
                        break
                    elif arr[nr][nc] == 0:
                        nr += dr
                        nc += dc
                        cnt += 1
                    else:
                        if cnt >= 2:
                            edges.append((cnt, arr[i][j], arr[nr][nc]))
                        break
heapq.heapify(edges)
parent = [-1] * (island + 1)
answer = 0
connected = 3
while edges:
    weight, start, end = heapq.heappop(edges)
    if find_parent(start) != find_parent(end):
        union(start, end)
        answer += weight
        connected += 1
        if connected == island:
            print(answer)
            break
else:
    print(-1)