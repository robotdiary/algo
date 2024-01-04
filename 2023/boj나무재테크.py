from collections import deque

n, m, k = map(int, input().split())
plus = [list(map(int, input().split())) for _ in range(n)]
arr = [[5] * n for _ in range(n)]
trees = [deque() for _ in range(n ** 2)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[(x - 1) * n + (y - 1)].append(z)  # 나이
# 나무 정렬
for tree in range(n ** 2):
    trees[tree] = deque(sorted(trees[tree]))

for year in range(k):
    for i in range(n):
        for j in range(n):
            if trees[i * n + j]:
                dead_trees = []
                # 나무 성장(봄)
                for aging in range(len(trees[i * n + j])):
                    current = trees[i * n + j].popleft()
                    if current <= arr[i][j]:
                        arr[i][j] -= current
                        trees[i * n + j].append(current + 1)
                    else:
                        dead_trees.append(current)
                # 죽은 나무 양분화(여름)
                for d in dead_trees:
                    arr[i][j] += d // 2
            # 양분 추가(겨울)
            arr[i][j] += plus[i][j]
    # 번식(가을)
    for i in range(n):
        for j in range(n):
            for k in trees[i * n + j]:
                if not k % 5:
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                        if 0 <= i + dr < n and 0 <= j + dc < n:
                            trees[(i + dr) * n + (j + dc)].appendleft(1)
answer = 0
for ans in trees:
    answer += len(ans)
print(answer)