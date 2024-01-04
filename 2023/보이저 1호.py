n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
ans = 0  # 방향
answer = 0  # 시간
d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}  # 시작방향
r, c = map(lambda x: int(x) - 1, input().split())  # 시작 위치 인덱스 조정 해야함
# visited = [[0] * m for _ in range(n)]  # 초기화!!!!!!!!!!!!!!!!!!!!!!!!!
flag = 0  # 무한으로 즐기는지 visited와 flag로 확인

for start in 'URDL':  # 네 방향을 돌아 보고 최대를 찾을 것임
    visited = [[0] * m for _ in range(n)]  # 초기화!!!!!!!!!!!!!!!!!!!!!!!!!
    direction = d[start]  # 시작 방향
    time = 1  # 1에서 시작 ( 바로 블랙홀이어도 1이 걸리니까 )
    visited[r][c] = {direction}  # {(1, 0)}
    # visited에 출발 위치의 방향을 추가한 후, 다음 위치 탐색
    cr, cc = r + direction[0], c + direction[1]
    while 0 <= cr < n and 0 <= cc < m and arr[cr][cc] != 'C':
        # 다음 위치가 visited에 있고, 내가 갔던 방향이면 무한!
        if visited[cr][cc] != 0:
            if direction in visited[cr][cc]:
                flag = 'Voyager'
                break
            else:
                visited[cr][cc].add(direction)
        else:
            visited[cr][cc] = {direction}

        if arr[cr][cc] == '/':
            direction = (-direction[1], -direction[0])
        elif arr[cr][cc] == '\\':
            direction = (direction[1], direction[0])
        cr += direction[0]
        cc += direction[1]
        time += 1

    if flag:
        print(start)
        print(flag)
        break

    if time > answer:
        answer = time
        ans = start
else:
    print(ans)
    print(answer)