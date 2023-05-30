# 경로찾기
def dfs(start, end):  # 0, 2
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()  # 0
        if node not in visited:
            visited.add(node)
            for z in range(n):
                if arr[node][z]:
                    if z == end:
                        answer[start][end] = 1
                        return
                    stack.append(z)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            dfs(i, j)
        else:
            answer[i][j] = 1
for ans_list in answer:
    print(*ans_list)