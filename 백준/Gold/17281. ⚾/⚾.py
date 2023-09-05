import sys
input = sys.stdin.readline


def perm(depth, lst):
    if depth == 8:
        lst.insert(3, 0)
        baseball(lst)
        return

    for i in range(1, 9):
        if not visited[i]:
            visited[i] = 1
            perm(depth + 1, lst + [i])
            visited[i] = 0


def baseball(lst):
    global answer
    out = 0
    score = 0
    hitter = 0
    inning = 0
    first, second, third = 0, 0, 0
    while inning < n:
        go = scores[inning][lst[hitter % 9]]
        if go == 0:
            if out == 2:
                out = 0
                hitter += 1
                inning += 1
                first, second, third = 0, 0, 0
                continue
            out += 1
        else:
            if go == 1:
                score += third
                first, second, third = 1, first, second
            elif go == 2:
                score += second + third
                first, second, third = 0, 1, first
            elif go == 3:
                score += first + second + third
                first, second, third = 0, 0, 1
            else:
                score += 1 + first + second + third
                first, second, third = 0, 0, 0
        hitter += 1
    answer = max(answer, score)


n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

answer = 0
visited = [0] * 10
perm(0, [])
print(answer)