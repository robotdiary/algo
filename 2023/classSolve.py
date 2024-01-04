R, C, M = map(int, input().split())
R1, C1, R2, C2 = (R - 1), (C - 1), 2 * (R - 1), 2 * (C - 1)
lst = [list(map(int, input().split())) for _ in range(M)]
shark = [[None] * C for _ in range(R)]
for r, c, s, d, z in lst:
    if d == 1:
        shark[r-1][c-1] = (R2 - s % R2, 0, z)
    elif d == 2:
        shark[r-1][c-1] = (s % R2, 0, z)
    elif d == 3:
        shark[r-1][c-1] = (s % C2, 1, z)
    else:
        shark[r-1][c-1] = (C2 - s % C2, 1, z)

ans = 0
for cc in range(C):
    # print(*shark, sep='\n')
    # print()
    for cr in range(R):
        if shark[cr][cc]:
            ans += shark[cr][cc][2]
            shark[cr][cc] = None
            break

    new_shark = [[None] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if shark[r][c]:
                # if cc == 1:
                #     print(shark[r][c])
                s, d, z = shark[r][c]
                llkdkjfkdjdf = r
                if d == 0:
                    r += s
                    a, b = divmod(r, R1)
                    if a == 1 or a == 3:
                        r = R1 - b
                        s = R2 - s
                    else:
                        r = b
                else:
                    c += s
                    a, b = divmod(c, C1)
                    if a == 1 or a == 3:
                        c = C1 - b
                        s = C2 - s
                    else:
                        c = b

                if new_shark[r][c]:
                    if new_shark[r][c][2] < z:
                        new_shark[r][c] = (s, d, z)
                else:
                    new_shark[r][c] = (s, d, z)

    shark = new_shark

print(ans)