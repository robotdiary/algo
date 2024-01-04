'''
구현 52분
시간만 측정해보고 바로 제출 1분
(1차) 328 / 117668
(준호) 1 1 2 2 3 3 4 가 아니라 1 1 2 2 3 3 3 이라서 (0, 0)에 멈추지 않고 (0, -1)까지 가서
배열 밖으로 나가는 마지막 토네이도를 잘못 측정한다.
근데 0, -1로 가는 게 arr[0][-1]로 가서 이미 불어버린 토네이도 0을 보게 되어서 맞을 수 있었음!
'''
# 방향으로 이동 + 모래 옮기기
def move(r, c, time, d):
    global answer
    for go in range(time):
        r += di[d]
        c += dj[d]
        # print(r, c)
        # print(arr[r][c])
        one = arr[r][c] // 100
        two = arr[r][c] * 2 // 100
        five = arr[r][c] * 5 // 100
        seven = arr[r][c] * 7 // 100
        ten = arr[r][c] * 10 // 100
        rest = arr[r][c] - (sum((one, seven, ten, two) * 2) + five)
        sands = [one, one, seven, seven, ten, ten, two, two, rest, five]
        for i in range(10):
            dr, dc = r + sand[d][i][0], c + sand[d][i][1]
            if 0 <= dr < n and 0 <= dc < n:
                arr[dr][dc] += sands[i]
            else:
                answer += sands[i]
        arr[r][c] = 0
        # print(*arr, sep='\n')
        # print('===============')
    return r, c


di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
# 1, 1, 7, 7, 10, 10, 2, 2, a, 5
sand = {0: [(-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-2, 0), (2, 0), (0, -1), (0, -2)],
        1: [(-1, 1), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 1), (0, -2), (0, 2), (1, 0), (2, 0)],
        2: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-2, 0), (2, 0), (0, 1), (0, 2)],
        3: [(1, 1), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 1), (0, -2), (0, 2), (-1, 0), (-2, 0)]}

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# 달팽이 모양으로 움직이기
cr, cc = n//2, n//2
direction = 0
for turn in range(2, n * 2 + 1):
    cr, cc = move(cr, cc, turn // 2, direction)
    direction = direction + 1 if direction < 3 else 0

print(answer)