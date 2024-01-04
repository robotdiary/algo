def comb(depth, x):
    global answer

    if depth == half:
        start, link = 0, 0
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if visited[j]:
                        start += arr[i][j]
            else:
                for j in range(n):
                    if not visited[j]:
                        link += arr[i][j]
        answer = min(answer, abs(start - link))
        return

    for i in range(x, n):
        if not visited[i]:
            visited[i] = 1
            comb(depth + 1, i + 1)
            visited[i] = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
half = n // 2
answer = 987654321
for i in range(0, n - 4 + 1):
    visited[i] = 1
    comb(1, i + 1)
    visited[i] = 0
print(answer)