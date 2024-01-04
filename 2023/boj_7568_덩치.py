
n = int(input())
a = list(tuple(map(int, input().split())) for _ in range(n))
ranks = [1] * n
for i in range(n):
    cr, cc = a[i]
    for j in range(n):
        if cr < a[j][0] and cc < a[j][1]:
            ranks[i] += 1
print(*ranks)