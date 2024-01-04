'''
코어 수를 -로 세서 min(answer, (core, line))을 써보는 작전
depth도 코어 개수에서 -1로 들어가서 core - depth > answer[0]로 가지치기 하는 작전
-> 바깥 코어는 연결된 걸로 하고 안에만 도는게 빠르지
-> set은 원소가 많아질수록 합집합과 add에 더 많은 시간이 든다
'''
def dfs(depth, core, line, visited):  # 연결된 core 수 -로 세자
    global answer

    if core - depth > answer[0]:  # 가지치기
        return

    if not depth:  # 탈출 조건
        answer = min(answer, (core, line))
        return  # 이거 자꾸 빼먹네잉

    cr, cc = cores[n - depth]
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        cnt = 0  # 밖에 두면 네 방향의 cnt를 더해버린단다
        nr, nc = cr + dr, cc + dc  # dr dr로 하면 어떡하니
        visit = set()
        while 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == '0' and (nr, nc) not in visited and (nr, nc) not in visit:
                visit.add((nr, nc))
                nr += dr
                nc += dc
                cnt += 1
            else:
                break
        else:
            dfs(depth - 1, core - 1, line + cnt, visited | visit)
            # continue 필요 없
        dfs(depth - 1, core, line, visited)  # 연결 안 됐을 때 로직도 빼먹네잉


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                cores.append((i, j))

    n = len(cores)
    answer = (0, 0)  # 코어 수, 전선 길이
    dfs(n, 0, 0, set())
    print(f'#{tc} {answer[1]}')