for tc in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    answer = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and arr[i][j]:
                stack = [(i, j)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and arr[nr][nc]:
                            stack.append((nr, nc))
                            visited.add((nr, nc))
                answer += 1
    print(answer)