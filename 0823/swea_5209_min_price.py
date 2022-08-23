# 5209. 최소 생산 비용
def perm(depth, acc):
    global min_num
    if acc > min_num:
        return
    if depth == n:
        if min_num > acc: # 조건 걸어주고
            min_num = acc
            return # 리턴
    for i in range(n):
        if not check[i]:
            check[i] = 1
            perm(depth + 1, acc + arr[depth][i])
            check[i] = 0
    return min_num


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    check = [0] * n
    min_num = 99999
    print(f'#{tc} {perm(0, 0)}')