'''
풀이시간 1시간
구현 45분
'''
def check():
    acc = 0
    # 그룹 나누기
    groups = {}  # island : (칸 수, 숫자)
    visited = [[0] * N for _ in range(N)]
    island = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = island
                idx = 0
                stack = [(i, j)]
                while idx < len(stack):
                    cr, cc = stack[idx]
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == arr[i][j]:
                            stack.append((nr, nc))
                            visited[nr][nc] = island
                    idx += 1
                groups[island] = (len(stack), arr[i][j])
                island += 1
    # print('island', 'groups')
    # print(island, groups)
    # 맞닿은 변의 수 세기
    friends = {i: [0] * island for i in range(1, island)}
    for i in range(N):
        for j in range(N):
            for dr, dc in (0, 1), (1, 0):
                nr, nc = i + dr, j + dc
                if 0 <= nr < N and 0 <= nc < N and visited[i][j] != visited[nr][nc]:
                    friends[visited[i][j]][visited[nr][nc]] += 1
                    friends[visited[nr][nc]][visited[i][j]] += 1
    # print('friends')
    # print(friends)
    # 점수 계산하기
    for group in range(1, island-1):
        for team in range(group + 1, island):
            acc += (groups[group][0] + groups[team][0]) * groups[group][1] * groups[team][1] * friends[group][team]
    # print('더한 값', acc)
    return acc


def rotate(x, y, m):
    table = [arr[x+i][y:y+m] for i in range(m)]
    for i in range(m):
        for j in range(m):
            arr[x+i][y+j] = table[m-1-j][i]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
middle = N // 2
answer = 0
for tc in range(3):
    # [1] 점수 계산
    answer += check()

    # [2] 십자 반시계 90도 회전
    H = [arr[i][middle] for i in range(N)]
    V = arr[middle][::-1]
    for i in range(N):
        arr[i][middle] = V[i]
        arr[middle][i] = H[i]

    # [3] 네모 시계 90도 회전
    for i in range(0, N, middle+1):
        for j in range(0, N, middle+1):
            rotate(i, j, middle)

answer += check()
print(answer)