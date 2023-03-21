#  1953. [모의 SW 역량테스트] 탈주범 검거
destination = {
    '1': [(1, 0), (0, 1), (-1, 0), (0, -1)], # 하, 우, 상, 좌
    '2': [(1, 0), (-1, 0)], # 하, 상
    '3': [(0, 1), (0, -1)], # 좌, 우
    '4': [(-1, 0), (0, 1)], # 상, 우
    '5': [(1, 0), (0, 1)], # 하, 우
    '6': [(1, 0), (0, -1)], # 하, 좌
    '7': [(-1, 0), (0, -1)], # 상, 좌
}
T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
# 터널세로, 터널가로, 뚜껑세로, 뚜껑가로, 탈출소요시간
    arr = [list(map(int, input().split())) for _ in range(n)]
    q = [(r, c, 1)]
    visited = set({})
    depth = 1
    while q and depth <= l:  # 0 <= 3
        size = len(q)
        for _ in range(size):
            current = q.pop(0) # (2, 1)
            if current not in visited:
                visited.add((current[0], current[1]))
            for dr, dc in destination[str(arr[current[0]][current[1]])]:
                # 새로 갈 곳은 arr[current[0]+dr][current[1]+dc]
                # 새로 갈 곳이 범위 안이고, 방문하지 않은 곳이고, 파이프고, 갈 수 있는 파이프면 추가
                if 0 <= current[0]+dr < n and 0 <= current[1]+dc < m and (current[0]+dr, current[1]+dc) not in visited:
                    if arr[current[0]+dr][current[1]+dc] and (-dr, -dc) in destination[str(arr[current[0]+dr][current[1]+dc])]:
                        q.append((current[0]+dr, current[1]+dc, current[2]+1))
        depth += 1
    print(f'#{tc} {len(visited)}')

