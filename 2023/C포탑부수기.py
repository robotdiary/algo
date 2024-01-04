'''
1차 : 마지막 소트를 안 해줬다 + 내 위치 제외도 추가해줬다.
2차 : N * M을 N * N이라고 하다니...ㅎㅎ....
3차 : 메모리초과 내가 지나온 길 말고 그냥 전체 bfs가 공유하는 visited 필요
4차 :
'''
from collections import deque


def bfs(q, x, y):
    V = [[0] * M for _ in range(N)]

    while q:
        cr, cc, visited = q.popleft()
        if V[cr][cc] == 0:
            V[cr][cc] = 1
            for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                nr, nc = cr + dr, cc + dc
                nr %= N
                nc %= M
                if arr[nr][nc] > 0 and V[nr][nc] == 0:  # -로 안 가는지 확인 if arr[nr][nc]:로 바꾸자
                    if (nr, nc) == (x, y):
                        # print(visited)
                        return visited - {(-r, -c)}
                    q.append((nr, nc, visited | {(nr, nc)}))
    # 최단 거리 없으면
    visited = set()
    for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1):
        nr, nc = x + dr, y + dc
        nr %= N
        nc %= M
        if arr[nr][nc] > 0 and (nr, nc) != (-r, -c):  # 내가 아니
            visited.add((nr, nc))
    return visited


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
towers = []
for i in range(N):
    for j in range(M):  # 대충격
        if arr[i][j]:
            towers.append((arr[i][j], 0, -i - j, -j, -i))  # 공격력, -공격순서, -행-열, -열, -행

for tc in range(1, K + 1):
    if len(towers) == 1:
        break
    towers = deque(sorted(towers))
    # [1] 공격자 선정
    power, num, sm, c, r = towers.popleft()
    power += N + M  # 직접 올릴지 고민 일단은 아직 안 올림 <--
    p = power // 2
    # [2] 공격 대상 선정
    e_power, e_num, e_sm, e_c, e_r = towers.pop()

    # [3] 공격
    attacked = bfs(deque([(-r, -c, {(-r, -c)})]), -e_r, -e_c)
    for _ in range(len(towers)):
        p_power, p_num, p_sm, p_c, p_r = towers.popleft()
        if (-p_r, -p_c) in attacked:
            if p_power - p <= 0:
                arr[-p_r][-p_c] = 0
            else:
                arr[-p_r][-p_c] -= p
                towers.append((arr[-p_r][-p_c], p_num, p_sm, p_c, p_r))
        else:
            arr[-p_r][-p_c] += 1
            towers.append((arr[-p_r][-p_c], p_num, p_sm, p_c, p_r))
    # 공격자
    arr[-r][-c] = power
    towers.append((arr[-r][-c], -tc, sm, c, r))
    # 공격 대상
    if e_power - power <= 0:
        arr[-e_r][-e_c] = 0
    else:
        arr[-e_r][-e_c] -= power
        towers.append((arr[-e_r][-e_c], e_num, e_sm, e_c, e_r))

towers = sorted(towers)
print(towers[-1][0])