'''
50분 구현(35분) 고치기(10분)
뭐야뭐야 엄청난 에러!!!! IndexError: list index out of range
-> 나무가 하나도 없으면 망한다.
전엔 성장과 번식도 같이 하고, 제초도 더 깔끔해보인다 전 코드가 낫네
'''
N, M, K, C = map(int, input().split())
C += 1
arr = [list(map(int, input().split())) for _ in range(N)]
dead = [[0] * N for _ in range(N)]

answer = 0
for tc in range(M):
    # [1] 성장 - 인접 칸에 나무 있는 수 만큼
    flag = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                flag = 0
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                        arr[i][j] += 1

    ## 엣지 ## 나무가 하나도 없는 상황을 생각했어야지
    if flag:
        break

    # [2] 번식 - 벽, 다른 나무, 제초제 없는 곳에 (나//가능공간)만큼
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                friends = []
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 0 and dead[nr][nc] == 0:
                            friends.append((nr, nc))
                if friends:
                    baby = arr[i][j] // len(friends)
                    for br, bc in friends:
                        new_arr[br][bc] += baby
    for i in range(N):
        for j in range(N):
            arr[i][j] += new_arr[i][j]
    # print('나무 성장')
    # print(*arr, sep='\n')
    # [3] 제초할 자리 찾기
    mx = (0, 20, 20)  # 나무수, 좌표
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                cnt = arr[i][j]
                group = []
                for dr, dc in (1, 1), (1, -1), (-1, 1), (-1, -1):
                    for k in range(1, K + 1):
                        nr, nc = i + (dr * k), j + (dc * k)
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] > 0:
                                cnt += arr[nr][nc]
                            else:
                                break
                if cnt > mx[0]:
                    mx = (cnt, i, j)
    # print(*trees, sep='\n')
    # print(mx)

    # [4] 제초하기
    answer += mx[0]
    dead[mx[1]][mx[2]] = C  # 시작점 제초 안 찍었네
    arr[mx[1]][mx[2]] = 0  # 시작점 제초 안 찍었네
    for dr, dc in (1, 1), (1, -1), (-1, 1), (-1, -1):
        for k in range(1, K + 1):
            nr, nc = mx[1] + (dr * k), mx[2] + (dc * k)
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > 0:
                    arr[nr][nc] = 0
                    dead[nr][nc] = C
                else:
                    dead[nr][nc] = C
                    break

    # [5] 제초제 줄기
    for i in range(N):
        for j in range(N):
            if dead[i][j]:
                dead[i][j] -= 1
    # print(*dead, sep='\n')
    # print('제초한나무')
    # print(*arr, sep='\n')
print(answer)