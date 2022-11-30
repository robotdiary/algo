# 11725 트리의 부모 찾기
import sys
from collections import defaultdict
n = int(sys.stdin.readline())  # 노드의 개수 2~100000
trees = defaultdict(list)
for i in range(n-1):
    s, e = map(int, sys.stdin.readline().split())
    trees[s].append(e)
    trees[e].append(s)
stack = [1]
visited = set()
answer = [0] * (n + 1)
while stack:
    parents = stack.pop()
    if parents not in visited:
        visited.add(parents)
        for i in trees[parents]:
            if not answer[i]:
                answer[i] = parents
                stack.append(i)
# print(answer)
# for i in range(2, n + 1):             # 372ms 60400kb
#     print(answer[i])
print('\n'.join(map(str, answer[2:])))  # 344ms 66604kb
