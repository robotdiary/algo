from collections import deque
import heapq


def 경주(k, s):
    global rabbits
    # heapq.heapify(rabbits)
    rabbits = deque(sorted(rabbits))
    visited = set()
    for tc in range(k):
        # [1] 토끼 뽑아  점프수, 행+열, 행, 열, 고유번호
        # cnt, rc, r, c, num = heapq.heappop(rabbits)
        cnt, rc, r, c, num = rabbits.popleft()
        # [2] 갈 곳 찾아
        result = (2, 0, 0)  # sm, nr, nc
        dist = distance[num][0]
        # 왼쪽으로
        dc = (c + dist) % (M + M - 2)
        if dc >= M:
            dc -= dc - M + 1
        result = max(result, (r + dc + 2, r + 1, dc + 1))
        # 오른쪽
        dc = (c - dist) % (M + M - 2)
        if dc >= M:
            dc -= dc - M + 1
        result = max(result, (r + dc + 2, r + 1, dc + 1))
        # up
        dr = (r + dist) % (N + N - 2)
        if dr >= N:
            dr -= dr - N + 1
        result = max(result, (dr + c + 2, dr + 1, c + 1))
        # down
        dr = (r - dist) % (N + N - 2)
        if dr >= N:
            dr -= dr - N + 1
        result = max(result, (dr + c + 2, dr + 1, c + 1))

        # 점수 추가
        for key in distance:
            if key != num:
                distance[key][1] += result[0]
        # heapq.heappush(rabbits, (cnt + 1, result[0], result[1], result[2], num))
        rabbits.append((cnt + 1, result[0], result[1], result[2], num))
        visited.add(num)
    rabbits = sorted(rabbits)
    for i in range(len(rabbits)-1, -1, -1):
        if rabbits[i][4] in visited:
            distance[rabbits[i][4]][1] += s
            break


Q = int(input())

# [1] 경주 시작 준비
a = list(map(int, input().split()))
N, M, P = a[1], a[2], a[3]
distance = {}
rabbits = []  # 점프수, 행+열, 행, 열, 고유번호
for i in range(4, len(a), 2):
    distance[a[i]] = [a[i + 1], 0]
    rabbits.append((0, 0, 0, 0, a[i]))

for commands in range(Q - 2):
    command, K, S = map(int, input().split())
    # [2] 경주 진행
    if command == 200:
        경주(K, S)
    # [3] 이동 거리 변경
    else:
        distance[K] *= S

# [4] 최고의 토끼 선정
input()
answer = 0
for key, value in distance.items():
    answer = max(answer, value[1])

print(answer)
