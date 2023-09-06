import heapq

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
q = [(1, 0, 0, 0)]  # 칸, r, c, 쳤냐
visited = [[[987654321] * m for _ in range(n)] for _ in range(2)]
while q:
    acc, cr, cc, hit = heapq.heappop(q)
    if (cr, cc) == (n-1, m-1):
        print(acc)
        break
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m:
            if hit:
                if arr[nr][nc] == '0' and acc + 1 < visited[1][nr][nc]:
                    heapq.heappush(q, (acc + 1, nr, nc, 1))
                    visited[1][nr][nc] = acc + 1
            else:
                if arr[nr][nc] == '0' and acc + 1 < visited[0][nr][nc]:
                    heapq.heappush(q, (acc + 1, nr, nc, 0))
                    visited[0][nr][nc] = acc + 1
                elif arr[nr][nc] == '1' and acc + 1 < visited[1][nr][nc]:
                    heapq.heappush(q, (acc + 1, nr, nc, 1))
                    visited[1][nr][nc] = acc + 1

else:
    print(-1)