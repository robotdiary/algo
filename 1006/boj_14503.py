# boj 14503 로봇청소기 (G5)
n, m = map(int, input().split())  # 세로, 가로
r, c, d = map(int, input().split())  # 좌표, 방향 0북 1동 2남 3서
arr = [list(map(int, input().split())) for _ in range(n)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하, 우, 상, 좌
# input 받은 방향을 내가 원하는 설정한 방향으로 바꾸기
d_dict = {0: 2, 1: 1, 2: 0, 3: 3}
d = d_dict[d]  # 현재 바라보고 있는 방향
visited = []  # 청소한 영역
skip = 0  # 네 방향 다 skip되면 완료
while True:
    # 현재 위치를 청소한다
    if (r, c) not in visited:
        visited.append((r, c))
    # 왼쪽 탐색 (청소를 하건 안 하건 왼쪽으로 고개를 돌린다)
    d += 1
    # 갈 공간이 0이고, not visited면 이동
    if not arr[r+direction[d % 4][0]][c+direction[d % 4][1]] and (r+direction[d % 4][0], c+direction[d % 4][1]) not in visited:
        r += direction[d % 4][0]
        c += direction[d % 4][1]
        skip = 0  # 이동했다면 그동안 쌓인 skip(0<=skip<4) 초기화
        continue
    # 갈 공간이 1이거나, visited면 skip 했음을 알리고 다시 고개 돌리러 continue
    elif arr[r+direction[d % 4][0]][c+direction[d % 4][1]] or (r+direction[d % 4][0], c+direction[d % 4][1]) in visited:
        skip += 1
        # 네 번 skip했다면
        if skip > 3:
            # 한 칸 후진
            # 후진 못하면 종료
            if arr[r + direction[(d + 2) % 4][0]][c + direction[(d + 2) % 4][1]]:
                break
            else:
                r += direction[(d + 2) % 4][0]
                c += direction[(d + 2) % 4][1]
            skip = 0  # 후진했으면 skip 초기화
            continue
print(len(visited))