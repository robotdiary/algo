# 1시 - 13분
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]  # +는 오른쪽
for tc in range(int(input())):
    direction = 0  # 잊지 말고 % 4
    left, right = 0, 0
    top, bottom = 0, 0
    nr, nc = 0, 0
    for char in input():
        if char == 'F':
            nr += di[direction % 4]
            nc += dj[direction % 4]
            top, bottom = max(top, nr), min(bottom, nr)
            left, right = min(left, nc), max(right, nc)
        elif char == 'B':
            nr += di[(direction + 2) % 4]
            nc += dj[(direction + 2) % 4]
            top, bottom = max(top, nr), min(bottom, nr)
            left, right = min(left, nc), max(right, nc)
        elif char == 'L':
            direction -= 1
        else:
            direction += 1

    print(abs(top - bottom) * abs(right - left))