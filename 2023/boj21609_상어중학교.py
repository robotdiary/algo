'''
풀이 시간 : 1시간 8분
6분 : 구상
46분 : 구현 -> tc2 틀림 (우선 순위를 잘못 담음)
16분 : 디버깅

푸는 중 확인한 부분
    visited를 안 찍어서 무한루프
    - 시작점 안 찍음
    - visited는 일반블록만 처리하므로 무지개 블록의 방문을 확인할 수 없었음
    중력 작용
    - 아래에서 위로만 블록을 가져오면 블록 빈칸 빈칸 빈칸]일 때 블록을 한 칸만 내림
    - i, j에서 nr, nc로 바꾸면 그 부분의 모든 변수명을 확인해줘야 한다. 꼭 하나씩 빼먹더라고

tc로 확인한 부분
    아래쪽에서 공백을 6으로 지정, 위의 최대 그룹 찾는 함수에서 6처리를 안 해줌
    우선순위 정할 때, 순서를 이상하게 씀, 무지개가 먼전데 좌표를 먼저

다른 사람 코드에서 중력 부분을 살펴보자
문제가 명확한데도 한 두 군데 덜컥거리면서 한 번에 구현이 안 되는 부분이 문제
'''


def find_group():
    visited = [[0] * N for _ in range(N)]  # 일반 블록만 방문 처리 할 것
    selected = (2, 0, 0, 0, set())  # 크기, 무지개 수, 시작 좌표, 좌표 모음
    for i in range(N):
        for j in range(N):
            # dfs를 일반 블록에서 시작 (이 블록이 곧 기준 블록)
            if 0 < arr[i][j] < 6 and visited[i][j] == 0:
                stack = [(i, j)]
                visited[i][j] = 1  # 시작점 visited 까먹음 -> 무한루프
                group = {(i, j)}  # 무지개는 visited 안 찍으니까 확인해줘야함 -> 무한루프 -> 그룹으로 확인하면 visited 필요없을 것 같아 -> 이땐 필요없지만 새 기준블록을 찾을 때, 재방문 하지 않기 위해 필요함
                rainbow_cnt = 0
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and (nr, nc) not in group:
                            if arr[nr][nc] == arr[i][j]:
                                group.add((nr, nc))
                                visited[nr][nc] = 1
                                stack.append((nr, nc))
                            elif arr[nr][nc] == 0:
                                group.add((nr, nc))
                                stack.append((nr, nc))
                                rainbow_cnt += 1
                selected = max(selected, (len(group), rainbow_cnt, i, j, group))  # ? 순서 이상하게 둠
    return selected[4]  # 선택된 그룹만 반환


def move_down():
    for i in range(N-1):
        for j in range(N):
            nr, nc = i, j
            while 0 <= nr and 0 <= arr[nr][nc] < 6 and arr[nr+1][nc] == 6:

                arr[nr][nc], arr[nr+1][nc] = arr[nr+1][nc], arr[nr][nc]
                nr -= 1
    # -1 안 내려오고
    # 맨 위는 맨 아래까지 내려오고
    # 중간에 있어도 내려오고
    # 두 개 연속으로도 내려오고


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while True:
    # [1] 크기가 가장 큰 그룹 찾기 (무지개 최대)
    selected_group = find_group()
    if not selected_group:
        break

    # [2] 점수 획득 & 선택된 그룹 제거 -> 6으로
    answer += len(selected_group) ** 2
    for r, c in selected_group:
        arr[r][c] = 6

    # [3] 아래로 (검정 제외)
    move_down()

    # [4] 반시계 회전
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N-1-i]
    arr = new_arr

    # [5] 아래로
    move_down()

print(answer)
