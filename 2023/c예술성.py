'''
1차: 1시간 30분 구현 다 하고 접근 방법이 잘못 되었다는 걸 알았다.
2차: 끝나고 30분 동안 맞는 방법으로 다시 짜서 바로 통과
시간이 부족해서 못 풀면 너무 아쉬우니까 앞으로는 무조건 쉬운 문제부터 풀자!
그리고 교수님이 말씀해주신 것처럼 헷갈리는 난이도는 1시간(첫문제)/30분(다음문제)/그리고 두시간동안 진짜 하나만 파는 결정할 수 있도록 시간 분배를 잘 하자!
'''
from collections import defaultdict


def score():
    acc = 0
    # [1] 그룹화하기
    island = 11  # 그룹 이름
    first = {}  # 그룹 좌표 하나
    group = {}  # 그룹 숫자, 멤버수
    visited = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 0:
                visited[r][c] = island
                first[island] = (r, c)
                group[island] = [arr[r][c], 1]
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[nr][nc] == arr[r][c]:
                            stack.append((nr, nc))
                            visited[nr][nc] = island
                            group[island][1] += 1
                island += 1

    # [2] 인접 개수 찾기
    for key in first:
        q = [first[key]]
        # visit = {first[key]}
        visited[first[key][0]][first[key][1]] = 0
        friends = defaultdict(int)
        cnt = 1
        while q:
            cr, cc = q.pop()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if visited[nr][nc] == key:
                        q.append((nr, nc))
                        visited[nr][nc] = 0
                        cnt += 1
                    elif visited[nr][nc]:
                        friends[visited[nr][nc]] += 1

        for friend in friends:
            acc += (cnt + group[friend][1]) * group[key][0] * group[friend][0] * friends[friend]
    return acc


def turn(x, y):
    zip_arr = []
    for e in range(middle):
        zip_arr.append(arr[x + e][y:y + middle])
    zip_arr = list(zip(*zip_arr))
    for r in range(middle):
        for c in range(middle):
            new_arr[x + r][y + c] = zip_arr[r][-1 - c]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
middle = n // 2
answer = score()
for tc in range(3):
    new_arr = [[0] * n for _ in range(n)]
    # [1-1] 십자 돌리기
    for i in range(n):
        new_arr[i][middle] = arr[middle][-1 - i]
        new_arr[middle][i] = arr[i][middle]

    # [1-2] 90도 돌리기
    for i in (0, middle + 1):
        for j in (0, middle + 1):
            turn(i, j)
    # [2] 점수
    arr = new_arr
    answer += score()

print(answer)