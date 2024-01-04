'''
풀이시간 구상-8분 인풋만-5분 구현-60분 디버깅-30분
주의 :
    상어가 물고기를 먹으면서 이동하는데 원본 배열을 안 바꿀 것이므로
    같은 물고기를 먹지 않게
    그렇지만 이동은 가능하게
    잘 생각해보고 짜야한다 -> 갈 수는 있되, 먹었던 물고긴지 아닌지 확인하도록 수정

맨날 실수는 꼭 있냐 :
    시계방향 반시계방향 안 보고 시계방향으로 설정
    최대값 설정에서 최대값 보기만 하고 갱신 안 함
    최소값 설정에서 []빈배열로 해서 [1111]보다 작은 값이라 헛돔 [5555]해줘야함
     시간 쫄리는데 왜 계산 안 해봐
'''


def move(x, y, depth, direction, acc, visited):
    global mx_fishes, shark_move
    if depth == 3:
        if acc > mx_fishes:
            shark_move = direction
            mx_fishes = acc
        elif acc == mx_fishes:
            shark_move = min(shark_move, direction)
        return

    for nd in range(1, 5):
        nr, nc = x + shark_d[nd][0], y + shark_d[nd][1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            if (nr, nc) in visited:
                move(nr, nc, depth + 1, direction+[nd], acc, visited)
            else:
                move(nr, nc, depth + 1, direction+[nd], acc + len(table[nr][nc]), visited + [(nr, nc)])


M, S = map(int, input().split())
arr = [[[] for _ in range(4)] for _ in range(4)]
for idx in range(1, M + 1):
    X, Y, D = map(lambda x: int(x) - 1, input().split())
    arr[X][Y].append((idx, D))

sharks = tuple(map(lambda x: int(x) - 1, input().split()))
smells = [[0] * 4 for _ in range(4)]
di = (0, -1, -1, -1, 0, 1, 1, 1)
dj = (-1, -1, 0, 1, 1, 1, 0, -1)  # 왼쪽부터 qks시계 방향
shark_d = [0, (-1, 0), (0, -1), (1, 0), (0, 1)]

for tc in range(S):
    # [1] 물고기 복제
    table = [[[] for _ in range(4)] for _ in range(4)]
    # [2] 물고기 이동
    for i in range(4):
        for j in range(4):
            for fish, d in arr[i][j]:
                for dest in range(8):
                    nd = (d - dest) % 8
                    nr, nc = i + di[nd], j + dj[nd]
                    if 0 <= nr < 4 and 0 <= nc < 4 and smells[nr][nc] == 0 and (nr, nc) != sharks:
                        table[nr][nc].append((fish, nd))
                        break
                else:
                    table[i][j].append((fish, d))

    # [3] 상어 이동
    mx_fishes = 0
    shark_move = [5, 5, 5]  # [1, 2, 4]
    move(*sharks, 0, [], 0, [])
    cr, cc = sharks
    for m in shark_move:
        nr, nc = cr + shark_d[m][0], cc + shark_d[m][1]
        if table[nr][nc]:
            smells[nr][nc] = 3
            table[nr][nc] = []
        cr, cc = nr, nc
    sharks = (cr, cc)

    # [4] 냄새 사라지기 + [5] 물고기 복제
    for i in range(4):
        for j in range(4):
            if smells[i][j]:
                smells[i][j] -= 1
            table[i][j] += arr[i][j]

    arr = table

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(arr[i][j])

print(answer)