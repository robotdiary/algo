# boj 16234 인구이동(G5)
import copy

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
adj = arr
answer = 0
Flag = True
while True:
    for i in range(n):
        for j in range(n):
            arr = copy.deepcopy(adj)
            stack = [(i, j)]
            visited = {(i, j)}
            while stack:
                cr, cc = stack.pop()
                if (cr, cc) not in visited:
                    visited.add((cr, cc))
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited:
                        if l <= abs(arr[cr][cc] - arr[cr + dr][cc + dc]) <= r:
                            stack.append((cr + dr, cc + dc))
            s = 0
            for nr, nc in visited:
                s += arr[nr][nc]
            if s == arr[i][j]:
                continue
            average = s // len(visited)
            for nr, nc in visited:
                adj[nr][nc] = average
    else:
        if arr == adj:
            break
        else:
            answer += 1
print(answer)
