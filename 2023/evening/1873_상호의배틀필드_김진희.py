def find_car(height, width):
    for car_r in range(height):
        for car_c in range(width):
            if arr[car_r][car_c] == '^':
                return car_r, car_c, 'U'
            elif arr[car_r][car_c] == 'v':
                return car_r, car_c, 'D'
            elif arr[car_r][car_c] == '<':
                return car_r, car_c, 'L'
            elif arr[car_r][car_c] == '>':
                return car_r, car_c, 'R'


direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
d = {'U': '^', 'D': 'v', 'L': '<', 'R': '>'}
t = int(input())
for tc in range(1, t + 1):
    h, w = map(int, input().split())  # 맵 2~20
    arr = [list(input()) for _ in range(h)]
    n = int(input())
    user = input()
    # 일단 전차를 찾아
    cr, cc, arrow = find_car(h, w)  # 좌표, UDLR
    # 전차 자리는 평지고 나중에 출력할 때, 전차 위치에 표시해줄게
    arr[cr][cc] = '.'

    for char in user:
        if char == 'S':
            nr = cr + direction[arrow][0]
            nc = cc + direction[arrow][1]
            while 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '#':
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
                nr += direction[arrow][0]
                nc += direction[arrow][1]

        else:
            arrow = char
            nr = cr + direction[arrow][0]
            nc = cc + direction[arrow][1]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == '.':
                cr, cc = nr, nc
    # 전차의 위치에 전차 표시해주기
    arr[cr][cc] = d[arrow]
    print(f'#{tc}', end=' ')
    for answer in arr:
        print(*answer, sep="", end="\n")
