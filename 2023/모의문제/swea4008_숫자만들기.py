def calc(x, method, y):
    if method == 0:
        return x + y
    elif method == 1:
        return x - y
    elif method == 2:
        return x * y
    else:
        return int(x / y)


def cur(depth, acc):
    global mx, mn

    if depth == N:
        mx = max(mx, acc)
        mn = min(mn, acc)
        return

    for i in range(4):
        if not operation[i]:
            continue
        operation[i] -= 1
        cur(depth + 1, calc(acc, i, nums[depth]))
        operation[i] += 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    operation = list(map(int, input().split()))  # + - * /
    nums = list(map(int, input().split()))

    mx = -9999999
    mn = 9999999
    cur(1, nums[0])
    print(f'#{tc} {mx - mn}')
