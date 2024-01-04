# 소문난 칠공주
def search_seat(x):
    global answer
    stack = [(x[0][0], x[0][1])]
    visit = {(x[0][0], x[0][1])}
    while stack:
        cr, cc = stack.pop()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) in x and (nr, nc) not in visit:
                stack.append((nr, nc))
                visit.add((nr, nc))
                if len(visit) == 7:
                    answer += 1
                    return


def find_seven(cnt, Y, depth, lst):  # 좌표, 도연, 다솜
    if not depth:
        search_seat(lst)
        return
    for i in range(cnt, 25):
        r = i // 5
        c = i % 5
        if arr[r][c] == 'Y' and Y < 3:
            find_seven(i + 1, Y + 1, depth - 1, lst + [(r, c)])
        elif arr[r][c] == 'S':
            find_seven(i + 1, Y, depth - 1, lst + [(r, c)])


arr = [list(input()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
answer = 0

find_seven(0, 0, 7, [])

print(answer)