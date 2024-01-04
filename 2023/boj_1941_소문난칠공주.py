def check_seat(x):
    stack = [(x[0][0], x[0][1])]
    visited = {(x[0][0], x[0][1])}
    while stack:
        cr, cc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            if (cr + dr, cc + dc) in x and (cr + dr, cc + dc) not in visited:
                stack.append((cr + dr, cc + dc))
                visited.add((cr + dr, cc + dc))

    if len(visited) == 7:
        return 1
    else:
        return 0


def comb(depth, x, lst, cnt):
    global answer

    if depth == 7:
        answer += check_seat(lst)
        return

    for i in range(x, 25):
        if arr[i // 5][i % 5] == 'Y':
            if cnt < 3:
                comb(depth + 1, i + 1, lst + [(i // 5, i % 5)], cnt + 1)
        else:
            comb(depth + 1, i + 1, lst + [(i // 5, i % 5)], cnt)


arr = [list(input()) for _ in range(5)]
answer = 0
comb(0, 0, [], 0)
print(answer)