def 구름이동(r, c, d, s):
    # 새로운 좌표 찾기
    for destination in range(s):
        r += di[d]
        c += dj[d]
        if r == -1:
            r = n - 1
        elif r == n:
            r = 0
        if c == -1:
            c = n - 1
        elif c == n:
            c = 0
    arr[r][c] += 1
    visited.add((r, c))


def 물복사마법(water_lst):
    for r, c in water_lst:
        for pr, pc in (1, 1), (-1, -1), (-1, 1), (1, -1):
            pnr, pnc = r + pr, c + pc
            if 0 <= pnr < n and 0 <= pnc < n and arr[pnr][pnc] > 0:
                arr[r][c] += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 왼쪽부터 시계방향
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    direction, si = map(int, input().split())
    visited = set()  # 방금 구름이 이동한 자리로, 다음 구름이 생기지 않는 자리이자 물복사마법을 시행할 자리
    for cloud in range(len(clouds)):
        구름이동(*clouds.pop(), direction, si)
    물복사마법(visited)
    # 구름 생성
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in visited:
                clouds.append((i, j))
                arr[i][j] -= 2
answer = 0
for lst in arr:
    answer += sum(lst)
print(answer)