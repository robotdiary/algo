# 단지 번호 붙이기
def dfs(x, y):
    stack = [(x, y)]
    visited = {(x, y)}
    while stack:
        nr, nc = stack.pop()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= nr + dr < n and 0 <= nc + dc < n:
                if arr[nr + dr][nc + dc] and (nr + dr, nc + dc) not in visited:
                    stack.append((nr + dr, nc + dc))
                    visited.add((nr + dr, nc + dc))
                    arr[nr + dr][nc + dc] = 0
    nums.append(len(visited))


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
nums = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dfs(i, j)

print(len(nums))
for n in sorted(nums):
    print(n)