#abcde
n, m = map(int, input().split())
friends = [[] for _ in range(n)]
visited = [0] * n
flag = 0
for _ in range(m):
    start, end = map(int, input().split())
    friends[start].append(end)
    friends[end].append(start)


def find_friend(x, depth):
    global flag
    if not depth:
        flag = 1
        return
    for destination in friends[x]:
        if not visited[destination]:
            visited[destination] = 1
            find_friend(destination, depth - 1)
            if flag:
                return
            visited[destination] = 0


for i in range(n):
    visited[i] = 1
    find_friend(i, 4)
    visited[i] = 0

print(flag)
