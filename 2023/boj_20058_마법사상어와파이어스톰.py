'''
1시간 23분
돌리기까지 구현 : 49분
테케 3맞까지 구현 : 14분
디버깅 : 20분
-----------------------
출력이 헷갈리면 어떻게 하지…?
돌면서 삭제하지 말자 다 돌고 해라
(1차) 출력 잘못함
(2차) 668 / 117156
'''
n, q = map(int, input().split())
n = 2 ** n
arr = [list(map(int, input().split())) for _ in range(n)]
li = list(map(int, input().split()))

for tc in range(len(li)):
    l = 2 ** li[tc]
    rotate = [[0] * l for _ in range(l)]
    # 돌리기
    for i in range(0, n, l):
        for j in range(0, n, l):
            for k in range(l * l):
                rotate[k % l][l - 1 - (k // l)] = arr[i + (k // l)][j + k % l]
            for k in range(l * l):
                arr[i + (k // l)][j + k % l] = rotate[k // l][k % l]
    # print(f'======={tc}========')
    # print('=======돌림========')
    # print(*arr, sep='\n')

    # 얼음 녹이기
    ice = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                cnt = 0
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if not 0 <= nr < n or not 0 <= nc < n or arr[nr][nc] == 0:
                        cnt += 1
                        if cnt == 2:
                            ice.append((i, j))
                            break
    for mr, mc in ice:
        arr[mr][mc] -= 1
    # print(f'=======녹임========')
    # print(*arr, sep='\n')

sm = 0
for i in arr:
    sm += sum(i)
if sm:
    answer = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                mx = 1
                stack = [(i, j)]
                arr[i][j] = 0
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc]:
                            mx += 1
                            stack.append((nr, nc))
                            arr[nr][nc] = 0
                answer = max(answer, mx)
    print(sm)
    print(answer)
else:
    print(0)
    print(0)