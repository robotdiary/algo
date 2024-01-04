n, r, c = map(int, input().split())
acc = 0
answer = 0


def z(depth, x, y):
    global acc, answer
    if not depth:
        if (x, y) == (r, c):
            answer = acc
        acc += 1
        return

    for dr, dc in (0, 0), (0, 1), (1, 0), (1, 1):
        z(depth - 1, x + (2 ** (depth - 1) * dr), y + (2 ** (depth - 1) * dc))

        if answer:
            return
now = 2 ** n // 2
while now > 2:
    if r > now and c > now:
        acc
z(n, 0, 0)
print(answer)