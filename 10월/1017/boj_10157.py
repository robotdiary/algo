# 자리배정 s4
C, R = map(int, input().split())  # 가로개수 세로개수 7 6
arr = [[0] * C for _ in range(R)]
K = int(input())  # 11
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = [0]

k = 0  # 들어간 관객 수
d = 0  # 방향
cl, cr = R, 0  # 현재 위치
Flag = True
while Flag and K <= C * R:  # k가 좌석수보다 큰 수면 0출력
    while 0 <= cl + dr[d % 4] < R and 0 <= cr + dc[d % 4] < C and not arr[cl + dr[d % 4]][cr + dc[d % 4]]:
        cl += dr[d % 4]
        cr += dc[d % 4]
        k += 1
        arr[cl][cr] = k
        if k == K:
            answer = (cr + 1, R - cl)
            Flag = False
            break
    d += 1
print(*answer)