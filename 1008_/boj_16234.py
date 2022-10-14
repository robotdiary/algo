n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# while문 한 번이 하루
while True:
    Flag = 1  # arr에 변화가 있었다면 -1 해줄거고, 하나도 안 변하면 계속 1로 남아있을 것
    visited = set()  # 한 번 방문해서 인구수를 조정한 곳은 다시 안 들릴 것
    for i in range(n):
        for j in range(i % 2, n, 2):  # 전체 탐색은 시간초과 > 체스판(격자)처럼 돌면 절반의 횟수로 전체 검색 가능
            # DFS
            visit = set()  # dfs로 찍은 국경이 이어진 나라들
        if (i, j) not in visited:  # 한 번 방문해서 인구수를 조정한 곳은 다시 안 들릴 것
            stack = [(i, j)]
            s = 0  # 이어진 나라의 총 인구 수
            while stack:
                cr, cc = stack.pop()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited:
                        if l <= abs(arr[cr][cc] - arr[cr + dr][cc + dc]) <= r:
                            stack.append((cr + dr, cc + dc))  # 스택에 넣어줘야 하고
                            visited.add((cr + dr, cc + dc))  # 전체 방문에도 넣어줘야 하고
                            visit.add((cr + dr, cc + dc))  # 이어진 국경에도 넣어주고
                            s += arr[cr + dr][cc + dc]  # 인구수도 더해준다 (나중에 따로 하려면 연산이 추가되니까)
            if visit:  # 국경이 이어진 나라가 있다면
                Flag -= 1  # flag에 표시해주고
                visit.add((i, j))  # 시작점은 없으니까 추가 해준 뒤
                average = s // len(visit)  # 평균 인구를 구해서
                for nr, nc in visit:  # 이어진 나라들의 인구를 평균인구로 맞춰준다.
                    arr[nr][nc] = average  # 인구가 변화했지만 visited에 들어가서 뒤에 남은 다른
                    # 나라들이 안 들여다보니까 남은 탐색에 영향을 주지 않음

    if Flag == 1:  # == 더이상 인구 이동이 없었다면
        break  # 더이상 날짜를 셀 필요가 없지
    else:
        answer += 1  # 인구 이동이 있었다면 하루를 추가하고 다시 확인하러 가야지
print(answer)