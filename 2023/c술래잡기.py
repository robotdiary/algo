'''
2시간 30분 실패
    30분 : 바깥으로 도는 달팽이
    30분 : 안쪽으로 도는 달팽이
    60분 : 나머지 구현했는데 테케 틀려서 디버깅
1시간 50분
    10분 : 문제 읽기
    30분 : 달팽이  빼고 구현
    30분 : 바깥으로 가는 달팽이 구현
    30분 : 구현 끝
    30분 : 디버깅 (틀린 테케 보고 함ㅜㅜ)
1차 : 런타임에러 IndexError: list index out of range
    1. 달팽이 반대로 돌 때, direction을 초기화 안 해줬다
    2. 바깥 달팽이 돌 때, 범위 밖 체크를 or이 아니라 and로 해버림
    3. 잡은 녀석을 없애주지 않음
2차 : 런타임에러 IndexError: list index out of range ->2, 3번 문제 고치다가 1을 안 고친 채로 냈다
3차 : 틀렸습니다 ->달팽이 반대로 돌 때만 direction 초기화 함 반대도 해줘야지
4차 : 틀렸습니다 ->한 위치에 두 명의 도망자가 있을 수 있음을 처리 안 함!
5차 : 성공
'''
# 대박사건 같은 위치에 있을 수 있따!!
from collections import deque


def out_snail(x, y):
    global direction
    check = [[0] * N for _ in range(N)]
    mx = direction // 4 + 1
    dr = direction % 4
    nr, nc = x + di[dr], y + dj[dr]
    if middle - mx <= nr <= middle + mx and middle - mx <= nc <= middle + mx:
        if not middle - mx <= nr + di[dr] <= middle + mx or not middle - mx <= nc + dj[dr] <= middle + mx:
            direction += 1
        check[nr][nc] = 1
        return nr, nc


def in_snail(x, y):
    global direction
    dr = direction % 4
    nr, nc = x + di[dr], y + dj[dr]
    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        if not 0 <= nr + di[dr] < N or not 0 <= nc + dj[dr] < N or visited[nr + di[dr]][nc + dj[dr]] == 1:
            direction -= 1
        return nr, nc


N, M, H, K = map(int, input().split())
runners = deque()
for _ in range(M):
    X, Y, D = map(int, input().split())
    runners.append((X-1, Y-1, D))
trees = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(H))

# 도망자꺼
runner_d = ((0, -1), (0, 1), (1, 0), (-1, 0))  # 좌, 우, 아래, 위
oppo = {0: 1, 1: 0, 2: 3, 3: 2}

# 술래꺼
current = 1              # 달팽이 진행 방향
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)  # 상, 우, 하, 좌 / 0->  <-2
cr, cc = N // 2, N // 2  # 술래 좌표
direction = 0            # 술래가 보는 방향
middle = N // 2
visited = [[0] * N for _ in range(N)]  # 안쪽 달팽이에 쓰는 visited
visited[0][0] = 1

dead = set()  # 지난 턴에 잡힌 사람, 다음 턴에 빼고 움직일 것
answer = 0
for tc in range(1, K + 1):
    # 가지치기
    if not runners:
        break
    # [1] 도망자 이동
    move = [[0] * N for _ in range(N)]
    for runner in range(len(runners)):
        rr, rc, d = runners.popleft()
        if (rr, rc) not in dead:
            if abs(cr - rr) + abs(cc - rc) <= 3:
                nr, nc = rr + runner_d[d][0], rc + runner_d[d][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if (cr, cc) != (nr, nc):
                        rr, rc = nr, nc
                else:
                    d = oppo[d]
                    nr, nc = rr + runner_d[d][0], rc + runner_d[d][1]
                    if (cr, cc) != (nr, nc):
                        rr, rc = nr, nc
            runners.append((rr, rc, d))
            if (rr, rc) not in trees:
                move[rr][rc] += 1
    dead = set()  # 초기화

    # [2] 술래 이동
    if current:
        cr, cc = out_snail(cr, cc)
        if (cr, cc) == (0, 0):
            direction = 2
            current = 0
    else:
        cr, cc = in_snail(cr, cc)
        if (cr, cc) == (middle, middle):
            current = 1
            direction = 0
            visited = [[0] * N for _ in range(N)]
            visited[0][0] = 1

    # [3] 잡기
    for watch in range(3):
        nr, nc = cr + (watch * di[direction % 4]), cc + (watch * dj[direction % 4])
        if 0 <= nr < N and 0 <= nc < N and move[nr][nc] and (nr, nc) not in trees:
            answer += tc * move[nr][nc]
            dead.add((nr, nc))

print(answer)