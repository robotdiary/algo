def solution(cnt):
    ans = 0
    r, c = -1, -1
    for i in range(N):
        for j in range(N-M+1):  # 좀 덜 돌도록
            if j + M - 1 < N:  # -1 빼면 길이가 달라진다
                honey = arr[i][j:j+M]
                if 0 in honey:
                    continue
                if sum(honey) > C:
                    result = comb(honey)
                    if result > ans:
                        ans = result
                        r, c = i, j
                else:
                    acc = 0
                    for k in honey:
                        acc += k ** 2
                    if acc > ans:
                        ans = acc
                        r, c = i, j
    for k in range(M):
        arr[r][c + k] = 0
    if cnt:
        ans += solution(0)
    return ans


def comb(lst):
    ans = 0
    for i in range(1 << len(lst)):
        selected = []
        for j in range(len(lst)):
            if i & (1 << j):
                selected.append(lst[j])
        if sum(selected) <= C:
            acc = 0
            for k in selected:
                acc += k ** 2
            ans = max(ans, acc)
    return ans


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {solution(1)}')