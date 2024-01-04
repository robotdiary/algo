'''
[1] N개 선거구의 모든 부분집합을 구하고 (공집합 제외)
[2] 구역이 연결 되어 있는지 dfs로 확인
'''
def dfs(lst):
    stack = [lst[0]]
    visited = {lst[0]}
    while stack:
        current = stack.pop()
        for dest in adj[current]:
            if dest in lst and dest not in visited:
                stack.append(dest)
                visited.add(dest)
    if len(visited) == len(lst):
        return True
    return False


n = int(input())
people = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for i in range(n):
    a, *b = map(int, input().split())
    for j in b:
        adj[i].append(j - 1)  # 구역을 0부터로 하던, 1부터로 하던 통일
        # adj[i].extend(b)

answer = 987654321
for i in range(1, (1 << n) - 1):
    selected = []
    another = []
    for j in range(n):
        if i & (1 << j):
            selected.append(j)
        else:
            another.append(j)

    if dfs(selected) and dfs(another):
        acc = 0
        for plus in selected:
            acc += people[plus]
        answer = min(answer, abs(acc - (sum(people) - acc)))

if answer == 987654321:
    print(-1)
else:
    print(answer)