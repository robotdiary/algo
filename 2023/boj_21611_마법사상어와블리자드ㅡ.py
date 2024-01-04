'''
118268	328
총 풀이 시간 : 1시간 53분 → tc 답은 다 맞았는데 배열 결과가 다름
14분 구상
28분 다른 방법으로 전환
71분 구현 tc4 틀림
끝난 후 디버깅

[메모]
스피드가 필요한 순간!
달팽이 안쪽, 바깥쪽, 바깥으로 돌면서 안쪽 확인
마지막 숫자 넣지 않은 채 while문이 끝났을 때, 마지막 숫자도 넣어줘야 함 다만, 조건에 맞는다면!

[아이디어]
구슬을 움직일 때는, 바깥에서 안쪽으로 확인할 수 있는
나보다 한 칸 작은 칸의 좌표를 가진 in_snail배열을 생성해서 사용
'''


def snail_in():  # 안쪽으로 가는 좌표를 안내하는 달팽이배열
    cr, cc = 0, -1
    go = N * 2
    direction = 1  # -1 쪽으로
    while go > 1:
        for g in range(go//2):
            nr, nc = cr + di[direction % 4], cc + dj[direction % 4]
            in_snail[cr][cc] = (nr, nc)  # 다음 좌표를 현재 위치에 저장
            cr, cc = nr, nc
        else:
            go -= 1
            direction -= 1


# 구슬 안쪽으로 이동 / 안에서 바깥으로 가는 달팽이
def move():  # 아 범위 끝이랑 방향 돌 때도 작동하나 불안한데 -> 확인
    cr, cc = shark[0] + 1, shark[1] - 1
    go = 4
    direction = 1  # +1 쪽으로
    while 0 <= cr < N and 0 <= cc < N:
        for g in range(go // 2):
            if arr[cr][cc]:
                nr, nc = (cr, cc)  # 0인 순간의 좌표를 저장 (미리 다음 좌표로 넘어가면 안 됌)
                while arr[in_snail[nr][nc][0]][in_snail[nr][nc][1]] == 0 and (nr, nc) != (shark[0], shark[1]-1):
                    nr, nc = in_snail[nr][nc]
                if arr[nr][nc] == 0:
                    arr[cr][cc], arr[nr][nc] = arr[nr][nc], arr[cr][cc]

            cr, cc = cr + di[direction % 4], cc + dj[direction % 4]
        else:
            go += 1
            direction += 1


def destroy():  # 안에서 밖으로 가다가 구슬 없으면 멈추는게 좋은데? -> 확인
    flag = 0
    cr, cc = shark[0], shark[1] - 1
    go = 3
    direction = 0  # +1 쪽으로

    cnt = 0
    target = -1
    group = []
    while 0 <= cr < N and 0 <= cc < N and arr[cr][cc]:
        for g in range(go // 2):
            if arr[cr][cc] == target:
                cnt += 1
                group.append((cr, cc))
            else:
                if cnt >= 4 > target:
                    flag = 1
                    answer[target] += cnt
                    for nr, nc in group:
                        arr[nr][nc] = 0

                target = arr[cr][cc]
                cnt = 1
                group = [(cr, cc)]

            cr, cc = cr + di[direction % 4], cc + dj[direction % 4]
        else:
            go += 1
            direction += 1
    if flag:
        return True
    return False


def solution():  # 새 배열을 만들 구슬 개수 세서 lst로 반환
    lst = []
    cr, cc = shark[0], shark[1] - 1
    go = 3
    direction = 0  # +1 쪽으로
    cnt = 0
    target = -1
    while 0 <= cr < N and 0 <= cc < N and arr[cr][cc]:
        for g in range(go // 2):
            if arr[cr][cc] == target:
                cnt += 1
            else:
                lst.append(cnt)
                lst.append(target)

                target = arr[cr][cc]
                cnt = 1

            cr, cc = cr + di[direction % 4], cc + dj[direction % 4]
        else:
            go += 1
            direction += 1
    # 마지막에 안 넣은 숫자가 있을 때, 추가 안 해줌
    if target:
        lst.append(cnt)
        lst.append(target)
    return lst


def make_arr(lst):  # 구슬 개수 센 lst로 새 배열 만들기
    idx = 2
    new_arr = [[0] * N for _ in range(N)]
    cr, cc = shark[0], shark[1] - 1
    go = 3
    direction = 0  # +1 쪽으로

    while 0 <= cr < N and 0 <= cc < N:
        for g in range(go // 2):
            if idx < len(lst):
                new_arr[cr][cc] = lst[idx]
                idx += 1
            else:
                return new_arr
            cr, cc = cr + di[direction % 4], cc + dj[direction % 4]
        else:
            go += 1
            direction += 1

    return new_arr


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = (1, 0, -1, 0)
dj = (0, 1, 0, -1)  # 하 우 상 좌
arrow = {1: 2, 2: 0, 3: 3, 4: 1}  # 상어 마법 방향을 내 di dj에 맞추기
shark = (N//2, N//2)

in_snail = [[0] * N for _ in range(N)]  # 안쪽 방향의 다음 달팽이 위치를 적어둔 배열
snail_in()

answer = [0] * 4
for tc in range(M):
    # [1] 구슬 파괴
    d, s = map(int, input().split())
    for k in range(1, s + 1):
        if 0 <= shark[0] + di[arrow[d]] * k < N and 0 <= shark[1] + dj[arrow[d]] * k < N:
            arr[shark[0] + di[arrow[d]] * k][shark[1] + dj[arrow[d]] * k] = 0
        else:
            break

    while True:
        # [2] 구슬 안쪽으로 이동
        move()

        # [3] 구슬 연속으로 4개 이상이면 폭발
        if not destroy():
            break

    # [4] 새로운 구슬로 다시 채우기
    arr = make_arr(solution())

print(answer[1] + answer[2] * 2 + answer[3] * 3)