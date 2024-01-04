from collections import deque
for tc in range(1, int(input()) + 1):
    W, H = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    answer = 0

    fires = deque()
    mans = deque()
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '*':
                fires.append((i, j))
            elif arr[i][j] == '@':
                mans.append((i, j))
                arr[i][j] = '.'  # 내 위치 초기화
                visited[i][j] = 1
    flag = 0
    while mans:
        # [1] 불 번지기
        for fire in range(len(fires)):
            fr, fc = fires.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = fr + dr, fc + dc
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == '.':
                    arr[nr][nc] = '*'
                    fires.append((nr, nc))
        # print(fires)
        # print(*arr, sep='\n')
        # print('=================')
        # [2] 도망치기
        for man in range(len(mans)):
            cr, cc = mans.pop()

            if cr in [0, H - 1] or cc in [0, W - 1]:
                flag = 1
                answer += 1
                print(answer)
                break
        #
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if arr[nr][nc] == '.' and visited[nr][nc] == 0:
                        mans.append((nr, nc))
                        visited[nr][nc] = 1

                else:
                    flag = 1
                    answer += 1
                    print(answer)
                    break
        else:
            answer += 1
    # print(*arr, sep='\n')
    # print('=================')
        if flag:
            break
        print(mans)

    else:
        print("IMPOSSIBLE")