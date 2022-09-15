# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 (D2)
def nodenum(i):
    if i <= n:
        nodenum(i * 2)
        nodenumlst.append(i)
        nodenum(i * 2 + 1)


# 루트와 부모 출력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    nodenumlst = []  # [4, 2, 5, 1, 6, 3]
    num = []  # [1, 2, 3, 4, 5, 6]
    for i in range(1, n+1):
        num.append(i)
    nodenum(1)
    root = num[nodenumlst.index(1)]
    node = num[nodenumlst.index(n//2)]
    print(f'#{tc} {root} {node}')
        # n = 1
        # while
        #     if tree[n] == 0:
        #         tree[n] = i
        #     elif i > tree[n]:
        #         n = tree[n * 2 + 1]
        #     else:
        #         n = tree[n * 2]