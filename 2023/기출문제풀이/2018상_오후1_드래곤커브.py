N = int(input())

di = (0, -1, 0, 1)
dj = (1, 0, -1, 0)  # 우 상 좌 하
oppo = {(0, -1): 1, (1, 0): 2, (-1, 0): 0, (0, 1): 3}
dragon = set()
for _ in range(N):
    X, Y, D, G = map(int, input().split())  # 좌표, 시작방향, 차수

    visited = [(X, Y), (X + di[D], Y + dj[D])]
    direction = [D]
    for go in range(G):
        for back in range(len(visited)-1, 0, -1):
            cr, cc = visited[back]
            nr, nc = visited[back-1]
            nd = oppo[(nr-visited[back][0], nc-visited[back][1])]
            visited.append((visited[-1][0] + di[nd], visited[-1][1] + dj[nd]))
            direction.append(nd)
    else:
        dragon |= (set(visited))

answer = 0
for r, c in dragon:
    if (r + 1, c) in dragon and (r, c + 1) in dragon and (r+1, c+1) in dragon:
        answer += 1
print(answer)
