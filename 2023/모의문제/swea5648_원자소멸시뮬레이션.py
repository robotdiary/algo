'''
X, Y 잘못 생각하기 쉽다. X Y 와 방향을 잘 맞춰서 받아야 함
가지치기 할 범위도 <=2000 인지 < 2000인지 정확히 해보자
'''
from collections import deque
di = (0, 0, -1, 1)
dj = (1, -1, 0, 0)

for tc in range(1, int(input()) + 1):
    N = int(input())
    cells = deque()
    for _ in range(N):
        X, Y, S, K = map(int, input().split())
        cells.append((X*2, Y*2, S, K))

    answer = 0
    for turn in range(4000):
        visited = set()
        removed = set()
        # [1] 위치 이동하면서 중복 위치는 없앤다 (먼저 가서 중복 체크 안 된애는 뒤에 없앰)
        for i in range(len(cells)):
            cr, cc, d, k = cells.popleft()
            nr, nc = cr + di[d], cc + dj[d]
            if (nr, nc) in visited:
                removed.add((nr, nc))
                answer += k
            else:
                visited.add((nr, nc))
                cells.append((nr, nc, d, k))

        for i in range(len(cells)):
            cr, cc, d, k = cells.popleft()
            if (cr, cc) in removed:
                answer += k
                continue
            if max(abs(cr), abs(cc)) <= 2000:
                cells.append((cr, cc, d, k))

        if len(cells) < 2:
            break

    print(f'#{tc} {answer}')