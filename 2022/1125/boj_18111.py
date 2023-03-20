N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
top = 0
bottom = 566
count = 0
answer = [0, 0]

while top > bottom:
    for i in arr:
        if max(i) > top:
            top = max(i)
        if min(i) < bottom:
            bottom = min(i)
    if top - bottom >= 3:
        if B > 0:
            for r in range(N):
                for c in range(M):
                    if arr[r][c] == bottom:
                        B -= 1
                        arr[r][c] += 1
                        count += 1
        else:
            check_top = False
            check_bottom = False
            Flag = True
            for r in range(N):
                if not Flag:
                    break
                for c in range(M):
                    if not check_top and arr[r][c] == top:
                        arr[r][c] -= 1
                    elif not check_bottom and arr[r][c] == bottom:
                        arr[r][c] += 1
                    if check_top and check_bottom:
                        count += 3
                        Flag = False
                        break
    elif top - bottom == 2:
        count += 3
        break
    else:
        cnt_top = 0
        cnt_bottom = 0
        for j in range(N):
            for z in range(M):
                if arr[j][z] == top:
                    cnt_top += 1
                elif arr[j][z] == bottom:
                    cnt_bottom += 1

        if cnt_top * 2 > cnt_bottom and B >= cnt_bottom:
            answer = [count + cnt_bottom, bottom + 1]
            break
        else:
            answer = [count + (cnt_top * 2), top - 1]
            break
print(*answer)