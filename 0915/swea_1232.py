# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산 (D4)
for tc in range(1, 11):
    v = int(input())
    tree = [0] * (v + 1)     # [0, '-', '-', 10, 88, 65]
    left = [0] * (v + 1)     # [0, 2, 4, 0, 0, 0]
    right = [0] * (v + 1)    # [0, 3, 5, 0, 0, 0]
    for i in range(v):
        info = list(input().split())
        if len(info) == 2:
            tree[int(info[0])] = int(info[1])
        else:
            tree[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
    for i in range(v, 0, -1):
        if tree[i] in ['+', '-', '*', '/']:
            if tree[i] == '+':
                tree[i] = tree[left[i]] + tree[right[i]]
            elif tree[i] == '-':
                tree[i] = tree[left[i]] - tree[right[i]]
            elif tree[i] == '/' and tree[right[i]] != 0.0:
                tree[i] = tree[left[i]] / tree[right[i]]
            else:
                tree[i] = tree[left[i]] * tree[right[i]]

    print(f'#{tc} {int(tree[1])}')
