def bfs():
    global answer
    visited = set()
    visited2 = set()
    for r in range(n):
        for c in range(n):
            if (r, c) not in visited:
                stack = [(r, c)]
                visited.add((r, c))
                cnt = 1
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (0, -1), (0, 1):  # 좌우만 탐색
                        if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited and arr[cr + dr][cc + dc] == arr[r][c]:
                            stack.append((cr + dr, cc + dc))
                            visited.add((cr + dr, cc + dc))
                            cnt += 1
                answer = max(answer, cnt)
            if (r, c) not in visited2:
                stack = [(r, c)]
                visited2.add((r, c))
                cnt = 1
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (-1, 0), (1, 0):  # 상하만 탐색
                        if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited2 and arr[cr + dr][cc + dc] == arr[r][c]:
                            stack.append((cr + dr, cc + dc))
                            visited2.add((cr + dr, cc + dc))
                            cnt += 1
                answer = max(answer, cnt)


n = int(input())
arr = [list(input()) for _ in range(n)]

answer = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(n):
    for j in range(n):
        if i + 1 < n and arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            bfs()
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

        if j + 1 < n and arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            bfs()
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

print(answer)