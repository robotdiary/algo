'''
49분
잔실수 빼고 바로 구현
'''
from collections import deque
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [0] 팀 찾기
teams = {}
island = 5  # 1-4는 배열 숫자랑 겹친다고
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = island
            q = deque([(i, j)])
            idx = 0
            while idx < len(q):
                cr, cc = q[idx]
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 2:
                        arr[nr][nc] = island
                        q.append((nr, nc))
                idx += 1
            else:  # 머리 꼬리 이어져있으면 순서 바뀐다고
                cr, cc = q[-1]
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 3:
                        arr[nr][nc] = island
                        q.append((nr, nc))
            teams[island] = q
            island += 1
# print(teams)
R, C, D = -1, 0, 0
di = (1, 0, -1, 0)
dj = (0, 1, 0, -1)

answer = 0
for tc in range(K):
    # [1] 한 칸 이동
    for key in teams:
        # 꼬리 떼기 -> 4로
        arr[teams[key][-1][0]][teams[key][-1][1]] = 4
        teams[key].pop()

        # 팀[0]에 인접 중 0이 아니면서 팀[1]이 아닌 칸 추가하기 -> 팀이름으로
        cr, cc = teams[key][0]
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 0 and (nr, nc) != teams[key][1]:
                    teams[key].appendleft((nr, nc))
                    arr[nr][nc] = key
                    break
    # print(*arr, sep='\n')

    # [2] 공 던지기
    # 범위 안이면 위치 바꾸고 공던지기
    # 범위 밖이면 방향만 바꾸고 공 던지기
    if not 0 <= R + di[D] < N or not 0 <= C + dj[D] < N:
        D = (D + 1) % 4
    else:
        R += di[D]
        C += dj[D]
    nd = (D + 1) % 4

    # [3] 최초로 맞은 사람 점수에 추가하고 머리 꼬리 변경
    for ball in range(N):
        nr, nc = R + (di[nd] * ball), C + (dj[nd] * ball)
        if 4 < arr[nr][nc]:
            answer += (teams[arr[nr][nc]].index((nr, nc)) + 1) ** 2
            teams[arr[nr][nc]] = deque(list(teams[arr[nr][nc]])[::-1])
            break

print(answer)