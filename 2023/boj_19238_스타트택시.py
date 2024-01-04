'''
2시간 30분
2분 : 문제 읽기, 선택
46분 : 구현 -> tc 실패
37분 : 디버깅 -> 틀렸습니다
48분 : 재구현 -> tc 틀림
14분 : 디버깅 -> 118044kb 284ms

<1차 풀이>
풀면서 놓친 부분
작은 행부터를 열로 생각해서 r, c가 꼬임
승객을 태운 후 소모한 연료 양 (전체 이동거리가 아님)
0으로 목적지에 도달하는 경우를 위해 cr, cc가 아닌 nr, nc가 답일 때로 탈출 조건을 내림
내리면서 변수명 바꾸지 않음

시작 지점에 손님 있는 것도 확인했고
연료가 0이 되면서 목적지에 도착할 때도 확인 했고
연료가 0이 되면서 승객 태우는 것도 봤고
시간은 계산 안 하고 제출
틀렸습니다

<2차 풀이>
못 찾겠어서 10:49분 아예 다시 짜기 시작
1차에 함수형으로 풀면서 어디서 잘못 return하는지를 못 찾았기 때문에
함수를 쓰지 않는 코드로 변경 나는 함수형을 못 짜는 걸까... 시무룩

풀면서 놓친 부분
찾은 승객 지워놓고 visited 찍기 빼먹음
템플릿 정신빼고 써서 줄 바꿔 쓰고
tc로 항상 승객을 찾는다고 생각해서 찾은 승객 리스트가 비어있을 때를 처리 안 함 고침
'''
from collections import deque


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cr, cc = map(lambda x: int(x) - 1, input().split())
goals = {}
for idx in range(2, M + 2):
    sr, sc, gr, gc = map(lambda x: int(x) - 1, input().split())
    arr[sr][sc] = idx
    goals[idx] = (gr, gc)
for _ in range(M):
    if K == 0:
        print(-1)
        break
    # 승객 찾기
    passengers = []
    if arr[cr][cc] >= 2:
        passengers.append((cr, cc, arr[cr][cc]))
    q = deque([(cr, cc)])
    visited = [[0] * N for _ in range(N)]
    visited[cr][cc] = 1
    while q and K and not passengers:
        for day in range(len(q)):
            r, c = q.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and  0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                    if arr[nr][nc] >= 2:
                        passengers.append((nr, nc, arr[nr][nc]))
                        visited[nr][nc] = 1 # 빼먹
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        K -= 1
    if K == 0:  # 필요없나
        print(-1)
        break
    if not passengers:  # 길이 다 가로 막혀서 손님이 없을 수도
        print(-1)
        break
    # 목적지 찾기 bfs
    def bfs(battery):
        stack = deque()
        visited = [[0] * N for _ in range(N)]
        goal = 0
        # 손님은 무조건 있다는 가정
        passengers.sort()
        arr[passengers[0][0]][passengers[0][1]] = 0
        visited[passengers[0][0]][passengers[0][1]] = 1
        goal = goals[passengers[0][2]]
        stack.append((passengers[0][0], passengers[0][1]))
        acc = 0
        while stack and battery:
            for day in range(len(stack)): # 아래랑 바꿔썼다
                r, c = stack.popleft()
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                        if (nr, nc) == goal:
                            return battery - 1, acc + 1, nr, nc
                        stack.append((nr, nc))
                        visited[nr][nc] = 1
            acc += 1
            battery -= 1
        return False
    result = bfs(K)
    if result:
        K, charge, cr, cc = result
        K += charge * 2
    else:
        print(-1)
        break

else:
    print(K)


# def 손님찾기(x, y, battery):
#     passengers = []
#     q = deque([(x, y)])
#     visited = [[0] * N for _ in range(N)]
#     visited[x][y] = 1
#     # 갈 데가 있고, 아직 손님 없고, 배터리가 있으면
#     while q and not passengers and battery:
#         for day in range(len(q)):
#             r, c = q.popleft()
#             for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and  0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
#                     if arr[nr][nc] >= 2:
#                         passengers.append((nr, nc, arr[nr][nc]))
#                         visited[nr][nc] = 1
#                         continue
#                     q.append((nr, nc))
#                     visited[nr][nc] = 1
#         else:
#             battery -= 1
#     if passengers:
#         passengers.sort()
#         arr[passengers[0][0]][passengers[0][1]] = 0
#         # print(*arr, sep='\n')
#         # print(passengers[0][2], '번 손님, 위치:', passengers[0][0], passengers[0][1], '배터리', battery)
#         return 목적지찾기(passengers[0][0], passengers[0][1], passengers[0][2], battery)
#     else:  # 배터리가 없다
#         return False
#
#
# def 목적지찾기(x, y, name, battery):
#     global cr, cc
#     q = deque([(x, y)])
#     visited = [[0] * N for _ in range(N)]
#     visited[x][y] = 1
#     acc = battery
#     while q and battery:
#         for day in range(len(q)):
#             r, c = q.popleft()
#             for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and  0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
#                     if (nr, nc) == goals[name]:
#                         cr, cc = nr, nc
#                         battery -= 1
#                         # print(name, '번 손님 목적지 위치:', goals[name], '배터리', battery)
#                         return battery, acc - battery
#                     q.append((nr, nc))
#                     visited[nr][nc] = 1
#         else:
#             battery -= 1
#     return False
#
#
# N, M, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cr, cc = map(lambda x:int(x) - 1, input().split())
# goals = {}
# for idx in range(2, M + 2):
#     sr, sc, gr, gc = map(int, input().split())
#     arr[sr-1][sc-1] = idx
#     goals[idx] = (gr-1, gc-1)
# # 손님이 있는 동안
# while M and K:  # 이거 for M으로 해야하나?
#     # 시작 시, 택시 위치에 손님이 있으면 바로 0
#     if arr[cr][cc] >= 2:
#         charge = 목적지찾기(cr, cc, arr[cr][cc], K)
#     # 없으면 손님 찾기
#     else:
#         charge = 손님찾기(cr, cc, K)
#
#     if charge:
#         K = charge[0] + charge[1] * 2
#         M -= 1
#         # print(K)
#     else:
#         print(-1)
#         break
# else:
#     print(K)