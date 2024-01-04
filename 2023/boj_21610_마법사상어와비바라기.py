'''
못 한 거
좌표 계산으로 찾으려고 오래 걸렸는데 잘 안 돼서 그냥 for문으로 전향  : 성공해서 시간줄일수있을까
물 +1 for문을 다 돌고 물복사마법을 해야하는데 한번에 하고싶은 마음에 잘 안보고 합쳐서 주려고 함
direction 1부턴데 자꾸 0부터로 하지마라
visited 원래 구름이 아니라 이동한 구름인데 원래 구름을 찍음 visited 신경써야지 왜 항상!!!
변수 이름이 많아지면 불안한 것 같다
시간 : 1시간 45분 (생각 15분 / 구현이 너무 오래 걸림, 사실상 구현을 한 번에 똑바로 정리 못해서 디버깅해가며 고치게 됐다)
'''
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