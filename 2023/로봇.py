m, n = map(int, input().split())  # 1000 1000
# 좌표 크기, 명령어 수
nr, nc = 0, 0
di = [0, -1, 0, 1]  # +1 => 오른쪽으로 돌기
dj = [1, 0, -1, 0]  # -1 => 왼쪽으로 돌기
direction = 0  # 잊지말고 %4
answer = [0]
for _ in range(n):
    command, d = input().split()
    d = int(d)
    if command == 'MOVE':
        nr += di[direction % 4] * d
        nc += dj[direction % 4] * d
        if not 0 <= nr < m or not 0 <= nc < m:
            answer = [-1]
            break
    else:
        if d:
            direction += 1
        else:
            direction -= 1
else:
    answer = [nc, nr]
print(*answer)