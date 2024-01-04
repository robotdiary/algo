n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
stack = [(0, 0, 0, 1)]
while stack:
    r1, c1, r2, c2 = stack.pop()
    if (r2, c2) == (n-1, n-1):
        answer += 1
        continue
    distance = (r2 - r1, c2 - c1)
    # 대각선일 때
    if distance == (1, 1):
        for dr, dc in (1, 0), (0, 1):
            nr, nc = r2 + dr, c2 + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
                stack.append((r2, c2, nr, nc))
    # 가로나 세로일 때
    else:
        nr, nc = r2 + distance[0], c2 + distance[1]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            stack.append((r2, c2, nr, nc))
    # 언제나
    for dr, dc in (1, 0), (0, 1), (1, 1):
        nr, nc = r2 + dr, c2 + dc
        if not 0 <= nr < n or not 0 <= nc < n or arr[nr][nc] != 0:
            break
    else:
        stack.append((r2, c2, r2 + 1, c2 + 1))
print(answer)