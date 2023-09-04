from collections import deque
for tc in range(int(input())):
    n = int(input())
    hr, hc = map(int, input().split())
    convi = [tuple(map(int, input().split())) for _ in range(n)]
    gr, gc = map(int, input().split())

    q = deque([(hr, hc)])  # 좌표, 골까지 거리
    visited = {(hr, hc)}
    while q:
        cr, cc = q.popleft()
        if abs(gr - cr) + abs(gc - cc) <= 1000:
            print('happy')
            break
        for nr, nc in convi:
            to_convi = abs(nr - cr) + abs(nc - cc)
            if to_convi <= 1000 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr,  nc))
    else:
        print('sad')