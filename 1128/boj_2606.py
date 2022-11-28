# 바이러스
from collections import defaultdict
n = int(input())  # 컴퓨터의 수 1부터 100이하
e = int(input())  # 간선 수
arr = defaultdict(list)  # 인자로 기본값의 형태 지정 가능
for i in range(e):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)  # 양쪽인거 놓침
stack = [1]
visited = set()
while stack:
    target = stack.pop()
    if target not in visited:
        visited.add(target)
        for i in arr[target]:
            stack.append(i)
print(len(visited)-1)


