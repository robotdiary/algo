n, m, cr, cc, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0] # 동 서 북 남
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
state = [1, 6, 4, 3, 5, 2]
answer = []
for d in command:
    nr, nc = cr + di[d], cc + dj[d]
    if 0 <= nr < n and 0 <= nc < m:
        # 움직일 수 있다면 실제 주사위 위치 변경
        cr += di[d]
        cc += dj[d]
        # 주사위 상태 바꾸기
        if d == 1:
            state = [state[2], state[3], state[1], state[0], state[4], state[5]]
        elif d == 2:
            state = [state[3], state[2], state[0], state[1], state[4], state[5]]
        elif d == 3:
            state = [state[4], state[5], state[2], state[3], state[1], state[0]]
        elif d == 4:
            state = [state[5], state[4], state[2], state[3], state[0], state[1]]

        # 판과 면의 숫자 옮겨 쓰기
        if arr[nr][nc]:
            dice[state[1]] = arr[nr][nc]
            arr[nr][nc] = 0
        else:
            arr[nr][nc] = dice[state[1]]
        answer.append(dice[state[0]])

print(*answer, sep='\n')
