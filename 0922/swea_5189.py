# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
def perm(depth):
    global answer
    if depth == n-1:
        # print(sel)
        # print('함수구분')
        acc = 0
        for i in range(n):
            # print('더할값', arr[sel[i]-1][sel[i+1]-1])
            acc += arr[sel[i]-1][sel[i+1]-1]
        # print('누적합', acc)
        if acc < answer:
            answer = acc
        return

    for i in range(1, n):
        if not check[i]:
            check[i] = 1
            sel[depth+1] = nums[i]
            perm(depth+1)
            check[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    nums = [i for i in range(1, n + 1)]
    check = [0] * n
    sel = [1] + [0] * (n - 1) + [1]
    answer = 10000
    perm(0)
    print(f'#{tc} {answer}')