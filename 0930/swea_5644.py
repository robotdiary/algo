# 5644. [모의 SW 역량테스트] 무선 충전
from collections import deque

move = {
    0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)
}

for tc in range(1, int(input()) + 1):
    m, a = map(int, input().split())  # 총 이동 시간, BC의 개수
    amove = list(map(int, input().split()))  # m개, 0 1상 2우 3하 4좌
    bmove = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    bc = [[] for _ in range(a)]
    
    # 배열 생성
    for _ in range(a):
        x, y, c, p = map(int, input().split())  # 좌표, 충전 범위, 처리량
        q = deque()
        q.append((y-1, x-1))
        visited = [(y-1, x-1)]
        arr[y-1][x-1] = p
        flag = c
        while flag:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = cr + dr
                    nc = cc + dc
                    if 0 <= nr < 10 and 0 <= nc < 10 and (nr, nc) not in visited:
                        if arr[nr][nc]:
                            arr[nr][nc] = (arr[nr][nc], p)
                        else:
                            arr[nr][nc] = p
                        visited.append((nr, nc))
                        q.append((nr, nc))
            flag -= 1
    # 이동
    man = (0, 0)  # arr[man[0]][man[1]]
    woman = (9, 9)  # arr[woman[0]][woman[1]]
    answer = 0
    for i in range(m):
        if man == woman:
            answer += arr[man[0]][man[1]]
        else:  # 충전 두 개 되는 지역이면, 위에서 좌표를 찍어놔야 겠다.
            if man in 좌표 or not woman in 좌표:



    print(arr)