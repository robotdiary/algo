# boj 1347 미로만들기 S3
n = int(input())
arr = [['#'] * (n * 2 + 1) for _ in range(n * 2 + 1)]  # 가운데에서 시작했을 때, 최대
info = input()
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # 우, 상, 좌, 하
# right = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌, 상, 우, 하
r, c = n, n  # 현재 위치 가운데
arr[49, 49] = '.'
# dr, dc = 1, 0  # 바라보고 있는 방향
drdc = 0
cnt = 0
for i in info:
    if i == 'F':
        arr[r+][c+]
        r += dr
        c += dc
    elif i == 'R':
        dr