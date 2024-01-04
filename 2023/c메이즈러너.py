'''
9시 30분 리팩토링 시작
9시 47분 참가자 이동 구현 (확인 안 함)
10시 40분 난 이제 못 하겠다
11시 20분 준호님이 응원해줌
'''
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 나만의 미로 만들기
maze = [[[]for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        maze[i][j].append(arr[i][j])

# 참가자 10부터
for idx in range(11, M + 11):
    x, y = map(lambda x: int(x) - 1, input().split())
    maze[x][y].append(idx)

# 출구
gr, gc = map(lambda x: int(x) - 1, input().split())
maze[gr][gc][0] = -1
# print(*maze, sep='\n')
answer = 0
for tc in range(K):
    # [1] 참가자 이동
    # [1-1] 참가자 좌표를 q에 넣고 0으로 만들기
    mans = deque()  # 좌표, 번호
    for i in range(N):
        for j in range(N):
            while 10 < maze[i][j][-1]:
                mans.append((i, j, maze[i][j].pop()))

    # [3] 참가자 모두 탈출했다면 종료
    if not mans:
        break
    # print('사람 좌표', mans)
    # [1-2] 좌표 popleft해서 위치 바꾸고 좌표에 맞춰 다시 사람 추가
    for man in range(len(mans)):
        cr, cc, num = mans.popleft()
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not 0 < maze[nr][nc][0] < 10 and abs(gr - nr) + abs(gc - nc) < abs(gr - cr) + abs(gc - cc):
                cr, cc = nr, nc
                answer += 1
                break
        if maze[cr][cc][0] != -1:
            maze[cr][cc].append(num)
    # print('========사람 이동=========')
    # print(*maze, sep='\n')

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited = [[0] * N for _ in range(N)]
        visited[sr][sc] = 1
        candidate = []
        time = 0
        while q and not candidate:
            for day in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                        if len(maze[nr][nc]) > 1:
                            candidate.append((nr, nc))
                            visited[nr][nc] = 1  # 이거 또 안 찍었네
                            continue
                        q.append((nr, nc))
                        visited[nr][nc] = 1
            else:
                time += 1
        if candidate:
            # candidate.sort()
            ans = []
            for mr, mc in candidate:
                mr, mc = max(mr, sr) - time, max(mc, sc) - time
                if mr < 0: mr = 0
                if mc < 0: mc = 0
                ans.append((mr, mc))
            ans.sort()
            return turn1(ans[0][0], ans[0][1], time)
        else:
            return False
            # print(tc)
            # print(*maze, sep='\n')
            # print('후보자가 없다니 뭔가 잘못됐다')


    def turn1(sr, sc, k):
        # print('온애', mr, mc, sr, sc, k)
        # mr, mc = max(mr, sr) - k, max(mc, sc) - k
        mr, mc = sr, sc
        # if mr < 0: mr = 0
        # if mc < 0: mc = 0
        new_arr = [[0] * (k + 1) for _ in range(k + 1)]
        result = ()
        # print('최소값이 잘 설정됐나 보자', mr, mc, '길이는', k + 1)

        for i in range(k + 1):
            for j in range(k + 1):
                new_arr[i][j] = maze[mr + k - j][mc + i]

        for i in range(k + 1):
            for j in range(k + 1):
                if 0 < new_arr[i][j][0] < 10:
                    new_arr[i][j][0] -= 1
                elif new_arr[i][j][0] == -1:
                    result = (mr + i, mc + j)
                maze[mr + i][mc + j] = new_arr[i][j]

        return result

    def turn(mr, mc, sr, sc, k):
        # print('온애', mr, mc, sr, sc, k)
        mr, mc = max(mr, sr) - k, max(mc, sc) - k
        if mr < 0: mr = 0
        if mc < 0: mc = 0
        new_arr = [[0] * (k + 1) for _ in range(k + 1)]
        result = ()
        # print('최소값이 잘 설정됐나 보자', mr, mc, '길이는', k + 1)

        for i in range(k + 1):
            for j in range(k + 1):
                new_arr[i][j] = maze[mr + k - j][mc + i]

        for i in range(k + 1):
            for j in range(k + 1):
                if 0 < new_arr[i][j][0] < 10:
                    new_arr[i][j][0] -= 1
                elif new_arr[i][j][0] == -1:
                    result = (mr + i, mc + j)
                maze[mr + i][mc + j] = new_arr[i][j]

        return result

    ans = bfs(gr, gc)
    if not ans:
        break
    gr, gc = ans
    # print('=======회전===========')
    # print(*maze, sep='\n')
    # print(answer)
print(answer)
print(gr + 1, gc + 1)