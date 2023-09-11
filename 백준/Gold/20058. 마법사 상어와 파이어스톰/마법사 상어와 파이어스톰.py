# print 0이 두 줄인가 혹시?
# arr 순회할 때, 제거하면서 지나가도 되는지 순회가 끝나고 제거해야하는지 확인
import sys
input = sys.stdin.readline

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