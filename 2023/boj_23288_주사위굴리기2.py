'''
총 풀이 시간 45분
1분 읽고 바로 먼저 풀 것으로 선택 ( 3분간 2번 읽고 역시 1번 풀러 ㄱㄱ )
바로 구현 : tc4 틀림 -> 만들어 놓은 딕트가 주사위 굴림에 따라 바뀌지 않음
1차 : 115964	284

다른 주사위 굴리는 방법 사용해보기
'''
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cr, cc = 0, 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 우 하 좌 상 시계방향
oppo = {0: 2, 2: 0, 1: 3, 3: 1}
d = 0
dice = (1, 4, 5, 3, 2, 6)

answer = 0
for tc in range(K):

    turn = {0: (dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]),
            2: (dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]),
            1: (dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]),
            3: (dice[2], dice[1], dice[5], dice[3], dice[0], dice[4])}
    # [1] 한 칸 이동, 범위 밖이면 반대로
    if not 0 <= cr + di[d] < N or not 0 <= cc + dj[d] < M:
        d = oppo[d]
    cr += di[d]
    cc += dj[d]

    # [2] 도착칸 점수 획득
    stack = [(cr, cc)]
    visited = {(cr, cc)}
    while stack:
        pr, pc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = pr + dr, pc + dc
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and arr[nr][nc] == arr[cr][cc]:
                stack.append((nr, nc))
                visited.add((nr, nc))
    answer += len(visited) * arr[cr][cc]

    # [3] 방향 정하기
    dice = turn[d]
    if dice[-1] > arr[cr][cc]:
        d += 1
        d %= 4
    elif dice[-1] < arr[cr][cc]:
        d -= 1
        d %= 4

    # 디버깅
    # print('dice:', dice, '바닥면:', dice[-1])
    # print('현재위치', cr, cc, '수', arr[cr][cc])
    # print('점수', visited)
    # print('방향', d)
print(answer)