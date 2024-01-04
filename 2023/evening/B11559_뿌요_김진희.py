def pop_puyo():
    puyo = 0
    for i in range(11, -1, -1):
        for j in range(6):
            if arr[i][j] != '.':
                target = arr[i][j]
                stack = [(i, j)]
                visited = {(i, j)}
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < 12 and 0 <= nc < 6 and (nr, nc) not in visited and arr[nr][nc] == target:
                            stack.append((nr, nc))
                            visited.add((nr, nc))
                    if len(visited) >= 4:
                        for r, c in visited:
                            arr[r][c] = '.'
                        puyo = 1
    return puyo


def move_puyo():
    for j in range(6):
        idx = 12
        for i in range(11, -1, -1):
            if idx > 11 and arr[i][j] == '.':
                idx = i
            elif idx < 12 and arr[i][j] != '.':
                arr[i][j], arr[idx][j] = arr[idx][j], arr[i][j]
                idx -= 1


arr = [list(input()) for _ in range(12)]
answer = 0
while pop_puyo():
    answer += 1
    move_puyo()
print(answer)
