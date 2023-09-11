n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs.append((ri-1, ci-1, mi, si, di))

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
for tc in range(k):
    arr = [[[0, 0, 0, -1] for _ in range(n)] for _ in range(n)]  # 힘, 속도, 개수, 방향
    # print(arr)
    for fireball in range(len(fireballs)):
        cr, cc, m, s, d = fireballs.pop()
        # 새 위치 찾기
        nr, nc = (cr + (di[d] * s)) % n, (cc + (dj[d] * s)) % n
        # 이동시키기
        arr[nr][nc][0] += m
        arr[nr][nc][1] += s
        arr[nr][nc][2] += 1
        if arr[nr][nc][2] == 1:
            arr[nr][nc][3] = d
        # 지금까진 같았는데, 이제 달라졌으면
        elif arr[nr][nc][3] < 8 and arr[nr][nc][3] % 2 != d % 2:
            arr[nr][nc][3] = 8
        # 달랐으면 다른대로 납두고, 계속 같아도 놔두고

    for i in range(n):
        for j in range(n):
            # 파볼 1개면 그대로
            if arr[i][j][2] == 1:
                fireballs.append((i, j, arr[i][j][0], arr[i][j][1], arr[i][j][3]))
            # 두 개 이상이고, 나눠도 힘이 남아있으면
            elif arr[i][j][2] > 1 and arr[i][j][0] // 5:
                if arr[i][j][3] == 8:
                    for dest in range(1, 8, 2):
                        fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], dest))
                else:
                    for dest in range(0, 8, 2):
                        fireballs.append((i, j, arr[i][j][0] // 5, arr[i][j][1] // arr[i][j][2], dest))
answer = 0
for ans in fireballs:
    answer += ans[2]
print(answer)