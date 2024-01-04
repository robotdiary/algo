'''
0차 : 오전 시간 안에 못 품 (아이디어를 간단하게 정리하지 못했다)
1차 : 틀렸습니다
2차 : 115592KB	152ms

놓친 것 :
    빨강이 먼저 빠져도 둘 다 빠지면 안 된다
    빨간공이 제자리일 수 있지 둘 다 같은 위치인 걸 visited삼자

이 문제에서 가져갈 포인트 : 구슬을 굴릴 때, 일단 쭉 다 굴리고 보기
    같은 위치라면 더 멀리서 온 애를 한 칸 뒤로 보내기
    구멍이라면 ~~ 처리 ... 이런 식으로 풀어나갈 수 있다.

이런 문제는 테케를 만들어보기가 너무 어렵다 어떻게 엣지케이스에 안 걸릴 수 있을까?
코드를 더 촘촘하게 짜야하는데
손으로 구슬을 따라가보면서 빨간 구슬과 파란 구슬의 visited를 어떻게 찍을지 좀 더 고민해봤어야 했다.
'''
from collections import deque


def move(nr, nc, dr, dc):
    dist = 0
    flag = 0
    while 0 <= nr + dr < N and 0 <= nc + dc < M and arr[nr + dr][nc + dc] != '#':
        nr += dr
        nc += dc
        dist += 1
        # 구멍이면 알려주자
        if arr[nr][nc] == 'O':
            flag = 1
            break
    return nr, nc, dist, flag


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
state = {}
# 위치 찾기 (벽 제외)
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if arr[i][j] == 'B':
            state['B'] = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            state['R'] = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            state['O'] = (i, j)

# q에 시작점 넣기
q = deque([(*state['R'], *state['B'])])
visited = {(*state['R'], *state['B'])}

# bfs
day = 1
Flag = 0
while q and day <= 10:
    for time in range(len(q)):
        a, b, c, d = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            redr, redc, redcnt, redflag = move(a, b, dr, dc)
            bluer, bluec, bluecnt, blueflag = move(c, d, dr, dc)
            # 제자리면? 방문한 곳이면? 둘 다 빠지면? -> 제자리거나 방문한 곳은 가능! 둘 다 빠지는게 안 됌
            if redflag and blueflag:
                continue
            # 같은 위치는 안 돼
            if redr == bluer and redc == bluec:
                if redcnt > bluecnt:
                    redr -= dr
                    redc -= dc
                else:
                    bluer -= dr
                    bluec -= dc

            # 구멍이면 탈출
            if (redr, redc) == state['O']:
                print(day)
                Flag = 1
                break
            if (bluer, bluec) == state['O']:
                continue
            if (redr, redc, bluer, bluec) not in visited:
                q.append((redr, redc, bluer, bluec))
                visited.add(((redr, redc, bluer, bluec)))
        if Flag:
            break
    else:
        day += 1
    if Flag:
        break
else:
    print(-1)
