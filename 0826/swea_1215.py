# 1215 회문
T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8):
        # [1] 가로 검사
            for z in range(n // 2):
                if j < 9-n and arr[i][j + z] != arr[i][j + n - 1 - z]:
                    break
                elif j >= 9-n: # 범위가 아닐 때도 카운트 된다 조건과 break 걸어줘
                    break
                else:
                    continue
            else:
                cnt += 1
        # [2] 세로 검사
            for z in range(n // 2): # i = 3, j = 7, n = 5, z = 0 1
                if i < 9-n and arr[i + z][j] != arr[i + n - 1 - z][j]:
                    break
                elif i >= 9-n:
                    break
                else:
                    continue
            else:
                cnt += 1
    print(f'#{tc} {cnt}')