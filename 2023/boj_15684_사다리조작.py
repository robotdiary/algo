'''
기존의 1번 사다리부터 cur(depth)로 사다리 만들면서 가는 구상은
뒤에 사다리를 추가했을 때, 앞 번호에서 출발한 결과를 바꾸게 만드니까 잘못되었다.
이 경우에는 사다리 0, 1, 2, 3개를 추가한 모든 경우를 돌아보고 찾는 것
'''


def ladder(cnt):
    global answer
    for i in range(M):
        flag = 0
        stack = [(0, i)]
        visited = [[0] * M for _ in range(N)]
        visited[0][i] = 1
        while stack:
            cr, cc = stack.pop()

            if arr[cr][cc][0] and visited[cr][cc-1] == 0:
                stack.append((cr, cc - 1))
                visited[cr][cc-1] = 1
            elif arr[cr][cc][1] and visited[cr][cc + 1] == 0:
                stack.append((cr, cc + 1))
                visited[cr][cc+1] = 1
            else:
                if cr + 1 == N:  # 미리 빼주기
                    if cc == i:
                        flag = 1
                        break
                else:
                    stack.append((cr + 1, cc))
                    visited[cr+1][cc] = 1
        if flag:
            continue
        return False

    answer = cnt
    return True


def comb(depth):
    if depth == 3:
        return ladder(3)

    for i in range(N):
        for j in range(M):
            # 사다리가 없으면
            if sum(arr[i][j]) == 0:
                # 왼쪽에 안 이어지면
                if 0 <= j-1 and arr[i][j-1][0] == 0:
                    arr[i][j][0] = 1
                    arr[i][j-1][1] = 1
                    if comb(depth + 1):
                        return True
                    if ladder(depth + 1):
                        return True
                    arr[i][j][0] = 0
                    arr[i][j - 1][1] = 0
                elif j+1 < M and arr[i][j + 1][1] == 0:
                    arr[i][j][1] = 1
                    arr[i][j + 1][0] = 1
                    if comb(depth + 1):
                        return True
                    if ladder(depth + 1):
                        return True
                    arr[i][j][1] = 0
                    arr[i][j + 1][0] = 0
    return False


M, K, N = map(int, input().split())  # 열, 사다리 수, 행 / 변수명 N, M, H 임의로 변환

arr = [[[0, 0] for _ in range(M)] for _ in range(N)]
for _ in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    arr[a][b][1] = 1
    arr[a][b + 1][0] = 1
# print(*arr, sep='\n')
answer = 4
if ladder(0):
    print(0)
else:
    if comb(0):
        print(answer)
    else:
        print(-1)