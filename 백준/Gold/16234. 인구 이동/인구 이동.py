'''
for j in range(i % 2, n, 2): 로 배열을 좀 덜 돌게 변경
종료 조건이 유동적이지 않도록, 방문 개수 판단에서 flag로 변경
'''
import sys
input = sys.stdin.readline

n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
nm = (n * n) // 2 + 1
answer = 0

while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i % 2, n, 2):
            if visited[i][j] == 0:
                stack = [(i, j)]
                visited[i][j] = 1  # 첫 녀석 visited 찍기 맨날 까먹네
                dfs = [(i, j)]
                sm = arr[i][j]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and  0 <= nc < n and visited[nr][nc] == 0:
                            if L <= abs(arr[cr][cc] - arr[nr][nc]) <= R:
                                stack.append((nr, nc))
                                visited[nr][nc] = 1
                                dfs.append((nr, nc))
                                sm += arr[nr][nc]
                if len(dfs) > 1:
                    flag += 1
                    avg = sm // len(dfs)
                    for r, c in dfs:
                        arr[r][c] = avg
    if flag:
        answer += 1
    else:
        break
print(answer)