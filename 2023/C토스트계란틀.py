'''
총 풀이시간 35분
20분 : 첫 구현으로 tc 실패
10분 : 종료 조건 디버깅 후 tc 성공
5분 : 시간 생각해보고 제출
-------------------------------
첫 녀석 visited 찍기를 생각하면서도 놓친다. 오늘은 dfs 배열에 넣어두고 visited처럼 생각해버렸다.
종료 조건이 n*n이 아니라 n*n+1으로 한 채 끝난다.
(1차) 성공
(2차) 격자로 확인해도 전체 확인이 가능하므로 for j in range(i % 2, n, 2): 로 배열을 좀 덜 돌게 변경 (676 -> 452ms)
     종료 조건이 유동적이지 않도록, 방문 개수 판단에서 flag로 변경
'''
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