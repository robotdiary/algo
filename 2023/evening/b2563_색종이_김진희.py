paper = set()
for _ in range(1, int(input()) + 1):
    c, r = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper.add((r + i, c + j))

print(len(paper))