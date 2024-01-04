from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

fishes = [0] * 7  # 인덱스(상어크기) 이하의 물고기 수
shark = (-1, -1)  # 상어 위치 좌표
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark = (i, j)
            arr[i][j] = 0


            def baby_shark(x, y):
                shark_size = 2
                eat = 0
                time = 0
                # 먹을 수 있는 애들이 있는 동안
                while True:
                    q = deque([(x, y)])
                    # visited = {(x, y)}
                    while q:
                        time += 1
                        can_eat = []
                        for day in range(len(q)):
                            cr, cc = q.popleft()
                            for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] <= shark_size:
                                    if 0 < arr[nr][nc] < shark_size:
                                        can_eat.append((nr, nc))
                                    elif arr[nr][nc] <= shark_size:
                                        q.append((nr, nc))
                                        visited.add((nr, nc))
                        if can_eat:
                            eatr, eatc = min(can_eat)
                            eat += 1
                            for i in range(arr[eatr][eatc], 7):
                                fishes[i] -= 1
                            arr[eatr][eatc] = 0
                            shark = (eatr, eatc)
                            if eat == shark_size:
                                eat = 0
                                if shark_size < 7:
                                    shark_size += 1
                            break

print(time)