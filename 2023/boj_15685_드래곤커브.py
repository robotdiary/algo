n = int(input())

di = [0, -1, 0, 1]  # 주어지는 시작 방향
dj = [1, 0, -1, 0]  # 주어지는 시작 방향
direction = {(1, 0): (0, -1),
             (0, 1): (1, 0),
             (-1, 0): (0, 1),
             (0, -1): (-1, 0)}
arr = [[0] * 101 for _ in range(101)]
mxr, mxc = 1, 1
for _ in range(n):
    y, x, d, g = map(int, input().split())
    curve = [(x, y), (x + di[d], y + dj[d])]
    for line in range(g):
        for dest in range(len(curve) - 1, 0, -1):
            cr, cc = curve[dest]
            dr, dc = direction[(curve[dest - 1][0] - curve[dest][0], curve[dest - 1][1] - curve[dest][1])]
            curve.append((curve[-1][0] + dr, curve[-1][1] + dc))
    for r, c in curve:
        arr[r][c] = 1
        mxr = max(mxr, r)
        mxc = max(mxc, c)

answer = 0
for i in range(mxr):
    for j in range(mxc):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            answer += 1
print(answer)