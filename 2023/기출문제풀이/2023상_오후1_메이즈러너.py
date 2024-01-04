'''
한시간 : 구현-30분 로직 다 썼는데, 로직이 잘못 된 걸 발견 / 30분 재구현 및 디버깅
똑같은 거 또 틀렸네 -> 사람과 벽이 같이 돌아가야해 ㅜㅜ
ii, jj를 i, j로 엄청 잘못 씀
'''
N, M, K = map(int, input().split())
arr = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
for idx in range(1, M + 1):
    X, Y = map(lambda x: int(x) - 1, input().split())
    arr[X][Y].append(idx)
R, C = map(lambda x: int(x) - 1, input().split())
arr[R][C][0] = -1

answer = 0
for tc in range(1, K + 1):
    # 1초마다 모든 참가자는 한 칸씩 움직입니다. 움직이는 조건은 다음과 같습니다.
    move = []
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 1:
                for p in range(len(arr[i][j]) - 1):
                    player = arr[i][j].pop()
                    cr, cc = i, j
                    dist = abs(cr - R) + abs(cc - C)
                    for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if abs(nr - R) + abs(nc - C) < dist and arr[nr][nc][0] < 1:
                            answer += 1
                            if arr[nr][nc][0] != -1:
                                move.append((player, nr, nc))
                            break
                    # 참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
                    else:
                        move.append((player, cr, cc))
    if not move:
        break
    for p, mr, mc in move:
        arr[mr][mc].append(p)
    # print(tc, '이동 후')
    # print(*arr, sep='\n')


    def turn():
        global R, C
        # 모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전합니다.
        # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
        size = 2
        while True:
            for i in range(N - (size - 1)):
                for j in range(N - (size - 1)):
                    flag = [0, 0]  # 참가자, 출구
                    for ii in range(size):
                        for jj in range(size):
                            if len(arr[i + ii][j + jj]) > 1:
                                flag[0] = 1
                            elif arr[i + ii][j + jj][0] == -1:
                                flag[1] = 1

                    if flag == [1, 1]:
                        # print('돌릴 위치')
                        # print(i, j, size)
                        block = [[[] for _ in range(size)] for _ in range(size)]
                        for ii in range(size):
                            for jj in range(size):
                                block[ii][jj] = arr[i+ii][j+jj][::]
                        # print(*block, sep='\n')
                        # 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.
                        for ii in range(size):
                            for jj in range(size):
                                if block[size - 1 - jj][ii][0] > 0:
                                    arr[i + ii][j + jj] = block[size - 1 - jj][ii][::]
                                    arr[i + ii][j + jj][0] -= 1
                                else:
                                    arr[i + ii][j + jj] = block[size - 1 - jj][ii][::]
                                    if arr[i + ii][j + jj][0] == -1:
                                        R, C = i + ii, j + jj
                        return
            size += 1
    turn()
    # print('돌린 후')
    # print(*arr, sep='\n')

print(answer)
print(R+1, C+1)