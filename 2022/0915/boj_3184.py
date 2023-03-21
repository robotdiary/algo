# 3184 양
def dfs(nr, nc, who):
    global answer
    sheep = 0
    wolf = 0
    if who == 'o': # 본인을 먼저 1 카운트 하고 사방 검색하러 가자
        sheep += 1
    else:
        wolf += 1
# [1] 우리가 배운 dfs와 구조 똑같음!
    stack = [(nr, nc)]
    visited = set()
    while stack:
        cr, cc = stack.pop()
        if (cr, cc) not in visited:
            visited.add((cr, cc))
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= cr+dr < r and 0 <= cc+dc < c and (cr+dr, cc+dc) not in visited:
# [2] 벽이 아닐 때만 쭉쭉 가고 벽이면 더이상 안 갈 것
                if arr[cr+dr][cc+dc] != '#':
                    stack.append((cr+dr, cc+dc))
# [3] 벽 안에 양이 있으면 양의 숫자를 세고, 센 양은 없앤다.
                    if arr[cr+dr][cc+dc] == 'o':
                        sheep += 1
                        arr[cr + dr][cc + dc] = '.'
# [4] 벽 안에 늑대 있으면 늑대 숫자를 세고, 센 늑대는 없앤다.
                    elif arr[cr+dr][cc+dc] == 'v':
                        wolf += 1
                        arr[cr + dr][cc + dc] = '.'
# [5] 영역 안에서 많은 애만 살아남는다. 적은 애는 죽었음
    if wolf >= sheep:
        answer[1] += wolf
    else:
        answer[0] += sheep
    return


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
answer = [0, 0] # 양, 늑대
# 전체를 탐색하면서 양이나 늑대를 만나면 DFS로 들어간다.
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'o':
            dfs(i, j, 'o')
        elif arr[i][j] == 'v':
            dfs(i, j, 'v')

print(*answer)

# arr = [[1, 2, 3], [3, 4, 5]]
# for i in range(2):
#     for j in range(2):
#         if arr[i][j] == 1 and j+1 < 3:
#             arr[i][j+1] = 1
# print(arr)

