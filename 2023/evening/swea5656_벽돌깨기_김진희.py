# 5656. [모의 SW 역량테스트] 벽돌 깨기
# 7시 18분 - 8시 50분
# 아니 바보야ㅠㅠㅠ 벽돌 숫자로 세면 어떻게 해ㅜㅜㅜㅠㅠㅠ  벽돌 개수를 세야지 어휴
from collections import deque


def crush(q, arr):
    new_arr = [arr[_][:] for _ in range(H)]
    while q:
        cr, cc, cnt = q.popleft()
        for day in range(cnt):
            for nd in range(4):
                nr, nc = cr + di[nd] * day, cc + dj[nd] * day
                if 0 <= nr < H and 0 <= nc < W and new_arr[nr][nc]:
                    if new_arr[nr][nc] > 1:
                        q.append((nr, nc, new_arr[nr][nc]))
                    new_arr[nr][nc] = 0
    return gravity(new_arr)


def gravity(new_arr):
    global answer
    for i in range(H-2, -1, -1):
        for j in range(W):
            if new_arr[i][j]:
                nr, nc = i, j
                while nr + 1 < H and new_arr[nr + 1][nc] == 0:
                    new_arr[nr][nc], new_arr[nr + 1][nc] = new_arr[nr + 1][nc], new_arr[nr][nc]
                    nr += 1
    return new_arr


def cur(depth, new_arr):
    global answer
    if depth == N:
        sm = 0
        for i in range(H):
            for j in range(W):
                if new_arr[i][j]:
                    sm += 1
        answer = min(answer, sm)
        return

    flag = 1
    for j in range(W):
        for i in range(H):
            if new_arr[i][j]:
                cur(depth + 1, crush(deque([(i, j, new_arr[i][j])]), new_arr))  #  ji바꼇다
                flag = 0
                break
    if flag:
        answer = 0
        return


di = (1, -1, 0, 0)
dj = (0, 0, -1, 1)
for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())

    answer = 9999
    cur(0, [list(map(int, input().split())) for _ in range(H)])

    print(f'#{tc} {answer}')