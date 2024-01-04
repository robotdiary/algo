n = int(input())
students = dict()
for _ in range(n ** 2):
    a, b, c, d, e = map(int, input().split())
    students[a] = {b, c, d, e}

arr = [[0] * n for _ in range(n)]
# 학생 번호로 돈다
for k in students:
    cr, cc, l, s = n + 1, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                likes, seats = 0, 0
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        # 좋아하는 친구면
                        if arr[nr][nc] in students[k]:
                            likes += 1
                        elif arr[nr][nc] == 0:
                            seats += 1
                if likes > l:
                    cr, cc, l, s = i, j, likes, seats
                elif likes == l and seats > s:
                    cr, cc, l, s = i, j, likes, seats
                elif likes == l and seats == s and cr > i:
                    cr, cc, l, s = i, j, likes, seats
    arr[cr][cc] = k  # 이걸 이상한 데 놨음
answer = 0
for i in range(n):
    for j in range(n):
        research = 0
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = i + dr, j + dc
            if 0 <= nr < n and 0 <= nc < n:
                # 좋아하는 친구면
                if arr[nr][nc] in students[arr[i][j]]:
                    research += 1
        # print()
        if research:
            answer += 10 ** (research - 1)

print(answer)