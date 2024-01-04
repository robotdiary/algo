'''
약간 귀신에 홀린 듯 중간에 잠깐 정신 잃은 채로 코드 쓰고 있었다.
잔 실수가 많다
'''
N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

kill = [[0] * N for _ in range(N)]
answer = 0

for tc in range(M):  # M인데 K라고 했다
    new_arr = [[0] * N for _ in range(N)]  # 이거랑 이걸 arr에 더할 위치를 나무 하나 안에다 적음
    tree_cnt = 0  # 나무가 하나도 없으면?
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                tree_cnt += 1
                # [0] 성장
                empty = []
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] > 0:
                            arr[i][j] += 1
                        elif arr[nr][nc] == 0 and kill[nr][nc] == 0:
                            empty.append((nr, nc))
                # [2] 번식
                for nr, nc in empty:
                    new_arr[nr][nc] += arr[i][j] // len(empty)
    if not tree_cnt:
        break

    for i in range(N):
        for j in range(N):
            arr[i][j] += new_arr[i][j]
    # print('=======성장과 번식')
    # print(*arr, sep='\n')

    # [3] 제초제 뿌릴 자리 찾기
    target_cnt = 0
    target = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:  # 나무가 있는 칸만이 아니라 모든 칸 중이지만 없는 칸은 0으로 끝남
                cnt = arr[i][j]
                group = [(i, j)]
                for dr, dc in (-1, -1), (1, -1), (-1, 1), (1, 1):
                    nr, nc = i, j
                    for k in range(K):
                        nr, nc = nr + dr, nc + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] > 0:
                                cnt += arr[nr][nc]
                                group.append((nr, nc))  # 이걸 안 썼음
                            else:
                                group.append((nr, nc))  # 빈칸이어도 제초제는 뿌려야 함 / 범위 안으로
                                break

                # 박멸하는 나무 수
                if cnt > target_cnt:
                    target = group
                    target_cnt = cnt
                # elif cnt == target_cnt and group[0][0] < target[0][0]:
                #     target = group
                # elif cnt == target_cnt and group[0][0] == target[0][0] and group[0][1] < target[0][1]:
                #     target = group
    answer += target_cnt
    # print('제초제 뿌릴 자리')
    # print(target_cnt, target)

    # [4] 있던 제초제 1년 깎기
    for i in range(N):
        for j in range(N):
            if kill[i][j]:  # 제초제를 깎아야하는데 나무를 깎았네?
                kill[i][j] -= 1

    # [5] 새 제초제 뿌리기
    for r, c in target:
        if arr[r][c] > 0:
            arr[r][c] = 0
        kill[r][c] = C  # 벽이어도 제초제는 상관없자나
    # print('=======1년 지난 후')
    # print(*arr, sep='\n')
    # print('=======제초제 상황')
    # print(*kill, sep='\n')
print(answer)