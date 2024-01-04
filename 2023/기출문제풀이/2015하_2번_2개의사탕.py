'''
백준 - 구슬 탈출 2
10월 2일 오전 9시 41분 - 10시 10분 (30분)
인풋 맞게 받기 무지성 map int input split 말고
N, M이 기본인데 N N에 절여져 있지 말기

잘 생각한 부분 :
    구슬 위치 찾고 빈칸으로 변경
    다음 위치 찾을 때, while 조건 nr, nc가 아니라 갈 위치(cr + di[d])로 설정
    같은 위치인 조건 생각해서 처리하기
    B먼저 탈출 확인해서 continue한 것
'''
from collections import deque


def find_next(x, y, d):
    cr, cc = x, y
    cnt = 0
    while 0 <= cr + di[d] < N and 0 <= cc + dj[d] < M and arr[cr + di[d]][cc + dj[d]] != '#':
        cr += di[d]
        cc += dj[d]
        cnt += 1
        if arr[cr][cc] == 'O':
            return cr, cc, cnt
    return cr, cc, cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# [0] 사탕 위치 찾기 (빈칸으로 바꿔주기)
red = ()
blue = ()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue = (i, j)
            arr[i][j] = '.'

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)
q = deque([(red, blue)])
flag = 0
for tc in range(10):
    for day in range(len(q)):
        r, b = q.popleft()
        for nd in range(4):
            # [1] 새 위치 찾기
            br, bc, bcnt = find_next(*b, nd)
            # [2] B의 새 위치가 출구면 실패
            if arr[br][bc] == 'O':
                continue
            # [3] R의 새 위치가 출구면 성공
            rr, rc, rcnt = find_next(*r, nd)
            if arr[rr][rc] == 'O':
                print(tc + 1)
                flag = 1
                break
            # [4] 탈출 못 하고 같은 위치로 왔으면 겹치지 않게 조정
            if (rr, rc) == (br, bc):
                if bcnt > rcnt:
                    br -= di[nd]
                    bc -= dj[nd]
                else:
                    rr -= di[nd]
                    rc -= dj[nd]
            # [5] 큐에 담기
            q.append(((rr, rc), (br, bc)))
        if flag:break
    if flag:break
else:
    print(-1)