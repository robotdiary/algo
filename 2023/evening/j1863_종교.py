# (2등) 300ms, 72840MB : 부모를 자식수로, 랭크로 깊이 체크
# def find(x):
#     if parent[x] < 0:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]
#
#
# def union(x, y):
#     # 랭크를 확인해서 랭크가 더 높은(자식 깊이가 깊은) 애한테
#     # 더 낮은 애를 붙인다.
#     if rank[x] > rank[y]:
#         # 자식 수를 늘리고
#         parent[x] += parent[y]
#         # 부모를 바꾸고
#         parent[y] = x
#     elif rank[x] == rank[y]:
#         rank[x] += 1
#         parent[x] += parent[y]
#         parent[y] = x
#     else:
#         parent[y] += parent[x]
#         parent[x] = y
#
#
# n, m = map(int, input().split())
# parent = [-1] * (n + 1)  # 부모는 0이하, 자식 수 카운트
# rank = [0] * (n + 1)  # 랭크는 깊이, 덜 깊어지도록 완화
# for tc in range(m):
#     a, b = map(int, input().split())
#     a = find(a)
#     b = find(b)
#     if a != b:
#         union(a, b)
#         n -= 1
# print(n)

# (1등) # 284ms, 72836MB : 원래 하던대로 부모자신, 랭크숫자
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    if rank[x] >= rank[y]:
        rank[x] += 1
        parent[y] = x
    else:
        rank[y] += 1
        parent[x] = y


n, m = map(int, input().split())
parent = list(range(n+1))
rank = [0] * (n + 1)
for tc in range(m):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)
        n -= 1
print(n)

# (4등) 363ms, 74012MB : 부모를 자신으로, 랭크 없음
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# n, m = map(int, input().split())
# parent = list(range(n+1))
# for tc in range(m):
#     a, b = map(int, input().split())
#     a = find(a)
#     b = find(b)
#     if a != b:
#         parent[b] = a
#         n -= 1
# print(n)

# (2등) 299ms, 73352MB : 부모 자신, 랭크 깊이
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# def union(x, y):
#     # 랭크를 확인해서 랭크가 더 높은(자식 깊이가 깊은) 애한테
#     # 더 낮은 애를 붙인다.
#     if rank[x] > rank[y]:
#         parent[y] = x
#     elif rank[x] == rank[y]:
#         rank[x] += 1
#         parent[y] = x
#     else:
#         parent[x] = y
#
#
# n, m = map(int, input().split())
# parent = list(range(n + 1))
# rank = [0] * (n + 1)  # 랭크는 깊이, 덜 깊어지도록 완화
# for tc in range(m):
#     a, b = map(int, input().split())
#     a = find(a)
#     b = find(b)
#     if a != b:
#         union(a, b)
#         n -= 1
# print(n)