# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # 사람 수, 신청서 수
    nums = list(map(int, input().split()))

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    for i in range(0, len(nums), 2):
        if find_set(nums[i]) != find_set(nums[i+1]):
            union(nums[i], nums[i+1])
    # 부모끼리 유니온 시, 자식들이 자동으로 따라가지 않는다. 따라서 다시 한 번 부모찾기
    for i in range(n + 1):
        find_set(i)

    parent = set(parent)
    print(f'#{tc} {len(parent)-1}')