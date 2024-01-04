import heapq

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
q = [(0, 0, 0)]  # r, c, 쳤냐
visited = [[[987654321] * m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1
while q:
    cr, cc, hit = heapq.heappop(q)
    if (cr, cc) == (n-1, m-1):
        print(visited[cr][cc])
        break
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < n and 0 <= nc < m:
            if hit:
                if arr[nr][nc] == '0' and visited[1][cr][cc] + 1 < visited[1][nr][nc]:
                    heapq.heappush(q, (nr, nc, 1))
                    visited[1][nr][nc] = visited[1][cr][cc] + 1
            else:
                if arr[nr][nc] == '0' and visited[0][cr][cc] + 1 < visited[0][nr][nc]:
                    heapq.heappush(q, (nr, nc, 0))
                    visited[0][nr][nc] = visited[0][cr][cc] + 1
                elif arr[nr][nc] == '1' and visited[1][cr][cc] + 1 < visited[1][nr][nc]:
                    heapq.heappush(q, (nr, nc, 1))
                    visited[1][nr][nc] = visited[1][cr][cc] + 1

else:
    print(-1)

# 메모리 초과
# import heapq
#
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# q = [(1, 0, 0, 0)]  # 칸, r, c, 쳤냐
# visited = {(0, 0, 0)}  # r, c, hit 으로 하고 visited.add할 땐 그냥 (r, c)로 해버렸다
# while q:
#     acc, cr, cc, hit = heapq.heappop(q)
#     if (cr, cc) == (n-1, m-1):
#         print(acc)
#         break
#     for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
#         nr, nc = cr + dr, cc + dc
#         if 0 <= nr < n and 0 <= nc < m:
#             if hit:
#                 if arr[nr][nc] == '0' and (nr, nc, 1) not in visited:
#                     heapq.heappush(q, (acc + 1, nr, nc, 1))
#                     visited.add((nr, nc, 1))
#             else:
#                 if arr[nr][nc] == '0' and (nr, nc, 0) not in visited:
#                     heapq.heappush(q, (acc + 1, nr, nc, 0))
#                     visited.add((nr, nc, 0))
#                 elif arr[nr][nc] == '1' and (nr, nc, 1) not in visited:
#                     heapq.heappush(q, (acc + 1, nr, nc, 1))
#                     visited.add((nr, nc, 1))
#
# else:
#     print(-1)