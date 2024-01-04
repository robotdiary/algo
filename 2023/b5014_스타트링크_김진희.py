# bfs 아이디어
from collections import deque
f, s, g, u, d = map(int, input().split())
answer = "use the stairs"

q = deque([(s, 0)])
visited = {s}
while q:
    current, push = q.popleft()
    if current == g:
        answer = push
        break

    if u and d:
        up = current + u
        down = current - d
        if up <= f and up not in visited:
            q.append((up, push + 1))
            visited.add(up)
        if down > 0 and down not in visited:
            q.append((down, push + 1))
            visited.add(down)
    elif u:
        up = current + u
        if up <= f and up not in visited:
            q.append((up, push + 1))
            visited.add(up)
    elif d:
        down = current - d
        if down > 0 and down not in visited:
            q.append((down, push + 1))
            visited.add(down)
print(answer)