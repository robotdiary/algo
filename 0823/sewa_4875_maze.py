# 4875 미로 (D2) 9:6 스택으로 재귀로?

# 벽이 없는 버전 :
T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 미로의 크기
    arr = [list(map(int, input())) for _ in range(n)]
    stack = []  # 위치인덱스를 튜플로 담을 것임
    visited = set()  # set 검색이 빠르다 O(1)
    dc = [0, 1, -1, 0]  # 아래, 우, 좌, 위
    dr = [1, 0, 0, -1]
    answer = 0  # 출력될 값

# [1] 시작 위치 찾는데 flag를 써봤다.
    for i in range(n):
        flag = True
        if 3 in arr[i]:
            stack.append((i, arr[i].index(3)))
            flag = False
            break
    while stack:
        r, c = stack.pop()  # 스택에 튜플로 담으면 r, c로 나눠서 할당 가능
        visited.add((r, c)) # set에는 add로 더하나봐

        if arr[r][c] == 2:
            answer = 1
            break

        for d in range(4):
            nr = r + dr[d]  # 벽이 없으니까 인덱스할 숫자를 지정해놓고
            nc = c + dc[d]  # 조건에 맞으면 그 때에 인덱스에 넣는다. 안 되면 튕겨
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            else:
                if arr[nr][nc] != 1 and arr[nr][nc] != 3:
                    if (nr, nc) not in visited:
                        stack.append((nr, nc))

    print(f'#{tc} {answer}')

# 벽이 있는 버전

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input()) # 미로의 크기
#     # 1로 감싸진 리스트 만들기
#     arr = [[1] * (n + 2)] + [[1] + list(map(int, input())) + [1] for _ in range(n)] + [[1] * (n + 2)]
#     stack = []
#     visited = []
#     dc = [0, 1, -1, 0]  # 아래, 우, 좌, 위
#     dr = [1, 0, 0, -1]
#     result = 0
#     for i in range(n):
#         if 3 in arr[i]:
#             # print(i, arr[i].index(3)) # == 1, 2 0으로 감싸져 있으니까
#             stack.append([i, arr[i].index(3)])
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
#         for i in range(4):
#             if arr[current[0] + dr[i]][current[1] + dc[i]] == 0 and [current[0] + dr[i], current[1] + dc[i]] not in visited:
#                 stack.append([current[0] + dr[i], current[1] + dc[i]])
#             elif arr[current[0] + dr[i]][current[1] + dc[i]] == 2:
#                 result = 1
#                 stack = []
#                 break
#     print(f'#{tc} {result}')


# 풀다 실패한 것
#     maze = [input() for _ in range(n)] # str
# # ['13101', '10101', '10101', '10101', '10021']
#     result = 0
#     stack = [] # '3'의 위치
#     visited = []
#     dc = [0, 1, -1, 0] # 아래, 우, 좌, 위
#     dr = [1, 0, 0, -1]
# # [1] 출발점 3을 찾는다.
#     for i in range(n):
#         if '3' in maze[i]:
#             stack.append([i, maze[i].find('3')])
# # [2] 출발점에서부터 네 방향으로 길을 찾는다.
#     while stack:
#         current = stack.pop() # [0, 1]
#         if current not in visited:
#             visited.append(current)
#         for destination in range(4):
# # [3] 검색 중 2가 있다면 반복문 탈출
#             try:
#                 if maze[current[0] + dr[i]][current[1] + dc[i]] == 2:
#                     result = 1
#                     stack = []
#                     break
# # [4] 검색 중 0이 있다면 자리 이동
#                 elif maze[current[0] + dr[i]][current[1] + dc[i]] == 0 and [current[0] + dr[i], current[1] + dc[i]] not in visited:
#                     stack.append([current[0] + dr[i], current[1] + dc[i]])
#             except:
#                 pass
#
#     print(f'#{tc} {result}')


# 확인해 본 것
# a= [1, 3, 1, 0, 1]
# print(a.index(3))

# aa = 'abcccde'
# print(aa.find('c'))

# stack = [1, 2, 3, 4, 5, 6]
# print(stack.pop(-2), stack.pop(-1))
