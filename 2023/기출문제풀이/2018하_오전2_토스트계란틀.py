'''
이 아니라 인구이동
'''


def solve():
    global arr
    new_arr = [[0] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] == 0:
                idx = 0
                q = [(i, j)]
                acc = arr[i][j]
                while idx < len(q):
                    cr, cc = q[idx]
                    for dr, dc in (1, 0), (0, -1), (0, 1), (-1, 0):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[cr][cc] - arr[nr][nc]) <= R and (nr, nc) not in q:
                            q.append((nr, nc))
                            acc += arr[nr][nc]
                            # print(arr[cr][cc], arr[nr][nc])
                    idx += 1

                if len(q) >= 2:
                    flag = False
                people = acc // len(q)
                for r, c in q:
                    new_arr[r][c] = people
    if not flag:
        arr = new_arr

    return flag


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while True:
    if solve():
        break
    answer += 1

print(answer)