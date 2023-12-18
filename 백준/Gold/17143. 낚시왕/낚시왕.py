'''
9시 56분 - 10시 48분 : 구현(26분) / 수정(26분)
new_arr을 봐야할 때, arr을 봐서 틀렸다.
'''
def find_next(cr, cc, s, d):
    arr[cr][cc] = 0  # 있던 애 없애
    gr, gc = cr + (di[d] * s), cc + (dj[d] * s)
    if d in [0, 1]:  # 상하면
        n = N + N - 2
        gr %= n
        if gr >= N:
            d = oppo[d]
        gr = saero[gr]
    else:  # 좌우면
        n = M + M - 2
        gc %= n
        if gc >= M:
            d = oppo[d]
        gc = garo[gc]

    gompangs[gompang] = (gr, gc, s, d)  # 정보 변경
    return gr, gc


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
gompangs = {}
for _ in range(K):
    X, Y, S, D, B = map(int, input().split())
    gompangs[B] = (X-1, Y-1, S, D-1)  # 좌표, 거리, 방향
    arr[X-1][Y-1] = B
di = (-1, 1, 0, 0)
dj = (0, 0, 1, -1)
oppo = {0: 1, 1: 0, 2: 3, 3: 2}
garo = [i for i in range(M)] + [i for i in range(M-2, 0, -1)]
saero = [i for i in range(N)] + [i for i in range(N-2, 0, -1)]
dead = set()

answer = 0
for tc in range(M):
    # [1] 아래로 먼저 만나는 곰팡이 채취
    for down in range(N):
        if arr[down][tc]:
            answer += arr[down][tc]
            dead.add(arr[down][tc])
            arr[down][tc] = 0  # 디버깅용
            break
            
    # [2] 이동
    new_arr = [[0] * M for _ in range(N)]
    for gompang in gompangs:
        if gompang not in dead:
            nr, nc = find_next(*gompangs[gompang])

            # 먼저 온 애 있으면 죽이고
            if new_arr[nr][nc]:
                if new_arr[nr][nc] > gompang:
                    dead.add(gompang)

                else:
                    dead.add(new_arr[nr][nc])  # 이거?
                    new_arr[nr][nc] = gompang
            else:
                new_arr[nr][nc] = gompang
    arr = new_arr
    
print(answer)
