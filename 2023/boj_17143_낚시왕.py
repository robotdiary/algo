'''
총 풀이 시간 : 150분
25분 : 상어 이동 빼고 구현
120분 : 상어 좌표를 계산으로 구하고 싶었는데 실패했다..
5분 : 상어를 좌표 탐색과 동시에 잡는 로직으로 바꿔보기
(1차) : 상어 잡고 들어가는 아래 코드 실패
(2차) : 평범하게 잡는 위 코드 통과
----------------------------------------
잘못 푼 부분
- 배열을 쓸지, deque를 쓸지, visited를 어디다 둘지 고민하면서 의식의 흐름대로 먼저 풀고보니
지난 문제랑 똑같은 방식인데도 왔다갔다하면서 다시 쓰게 된다. 실수할 수 있으니 왔다갔다 지양! 한 번에 짜기!

중간에 발견한 것
- input 받을 때, 리스트컴프리핸션 중독 때문에 r - 1, c - 1을 으악 이렇게 하기 싫어 하면서 10분 버린다 정신차려라

고민한 부분 : 로봇 청소기도 그렇고.. 이것도 다른 순서로도 성공하고 싶은데 왜 안 되는지조차 모르겠다...
>> 상어 위치 그대로 돌리면 시간이 너무 오래 걸릴 것 같아서 계산으로 구하고 싶었는데
 두 시간을 쏟아 부어도 안 되는 것....
 어차피 시간복잡도 계산해보면 문제 없으니까 시험에선 그냥 하라는대로 깔끔하게 하는 것에나 집중하자 <<
'''
from collections import deque


def move(x, y, distance, direction):
    for i in range(distance):
        nr, nc = x + di[direction], y + dj[direction]
        if 0 <= nr < n and 0 <= nc < m:
            x, y = nr, nc
        else:
            direction = turn[direction]
            nr, nc = x + di[direction], y + dj[direction]
            x, y = nr, nc
    return x, y, direction


n, m, k = map(int, input().split())
sharks = deque()
for _ in range(k):
    rr, cc, ss, dd, zz, = tuple(map(int, input().split()))
    sharks.append((rr - 1, cc - 1, ss, dd, zz))
answer = set()
di = (0, -1, 1, 0, 0)
dj = (0, 0, 0, 1, -1)
turn = {1: 2, 2: 1, 3: 4, 4: 3}

for man in range(m):
    visited = [[0] * m for _ in range(n)]
    catch = (100, 100, 0)
    # [1] 가까운 아래 상어 잡기
    for r, c, s, d, z in sharks:
        if c == man and r < catch[0]:
            catch = (r, c, z)
    answer.add(catch[2])

    # [2] 상어 이동
    for d in range(len(sharks)):
        r, c, s, d, z = sharks.popleft()
        if z in answer:
            continue
        r, c, d = move(r, c, s, d)
        if visited[r][c] == 0:
            visited[r][c] = (z, s, d)
        else:
            visited[r][c] = max(visited[r][c], (z, s, d))

    # [3] 상어 추가
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                sharks.append((i, j, visited[i][j][1], visited[i][j][2], visited[i][j][0]))
print(sum(answer))

'''
상어가 움직인 좌표를 돌 때 미리 다음 상어를 잡아놓는 작전
'''
# from collections import deque
#
#
# def move(x, y, distance, direction):
#     for i in range(distance):
#         nr, nc = x + di[direction], y + dj[direction]
#         if 0 <= nr < n and 0 <= nc < m:
#             x, y = nr, nc
#         else:
#             direction = turn[direction]
#             nr, nc = x + di[direction], y + dj[direction]
#             x, y = nr, nc
#     return x, y, direction
#
# n, m, k = map(int, input().split())
# sharks = deque()
# answer = set()
# mn = (999, 999, 0)
# for _ in range(k):
#     rr, cc, ss, dd, zz, = tuple(map(int, input().split()))
#     sharks.append((rr - 1, cc - 1, ss, dd, zz))
#     if cc - 1 == 0 and rr < mn[0]:
#         mn = (rr - 1, cc - 1, zz)
# answer.add(mn[2])
# di = (0, -1, 1, 0, 0)
# dj = (0, 0, 0, 1, -1)
# turn = {1: 2, 2: 1, 3: 4, 4: 3}
#
# for man in range(1, m):
#     # [1] 상어 이동
#     visited = [[0] * m for _ in range(n)]
#     for d in range(len(sharks)):
#         r, c, s, d, z = sharks.popleft()
#         if z in answer:
#             continue
#         r, c, d = move(r, c, s, d)
#         if visited[r][c] == 0:
#             visited[r][c] = (z, s, d)
#         else:
#             visited[r][c] = max(visited[r][c], (z, s, d))
#
#     # [2] 상어 추가
#     catch = (999, 999, 0)
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j]:
#                 sharks.append((i, j, visited[i][j][1], visited[i][j][2], visited[i][j][0]))
#                 if j == man and i < catch[0]:
#                     catch = (i, j, visited[i][j][0])
#     answer.add(catch[2])
# print(sum(answer))
