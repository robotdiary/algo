n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        stack = [(i, j, 1, arr[i][j], {(i, j)})]  # 좌표, 길이, 누적합, visited
        while stack:
            cr, cc, depth, acc, visited = stack.pop()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    if depth == 3:
                        answer = max(answer, acc + arr[nr][nc])
                    else:
                        stack.append((nr, nc, depth + 1, acc + arr[nr][nc], visited.union({(nr, nc)})))
        for turn in range(4):
            sm = arr[i][j]
            for d in range(3):
                tr, tc = i + di[(turn + d) % 4], j + dj[(turn + d)%4]
                if not 0 <= tr < n or not 0 <= tc < m:
                    break
                sm += arr[tr][tc]
            else:
                answer = max(answer, sm)
print(answer)