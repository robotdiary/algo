# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 (D3)
# def preorder(n):


T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for i in range(m):
        v, num = map(int, input().split())
        tree[v] = num
    for i in range(n, 0, -1):
        if i % 2:
            tree[i // 2] = tree[i] + tree[i-1]
        elif i + 1 >= len(tree):
            tree[i // 2] = tree[i]
        else:
            tree[i // 2] = tree[i] + tree[i + 1]
        # print(i, tree)
    # while n >= l and n > 1:
    #     if n % 2:
    #         tree[n // 2] = tree[n] + tree[n-1]
    #     elif n + 1 < len(tree):
    #         tree[n // 2] = tree[n] + tree[n + 1]
    #     else:
    #         tree[n // 2] = tree[n]
    #     n = n//2

    print(f'#{tc} {tree[l]}')