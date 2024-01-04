n = int(input())
arr = [list(input()) for _ in range(n)]

min_r, max_r = 9999, 0
min_idx, max_idx = 0, 0
min_c, max_c = 9999, 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            if min(i, n - i - 1) < min_r:
                min_r = min(i, n - i - 1)
                min_idx = i
            if min(j, n - j - 1) < min_c:
                min_c = min(j, n - j - 1)
                max_idx = j

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            max_r = max(max_r, abs(min_idx - i))
            max_c = max(max_c, abs(max_idx - j))

if not max_c and not max_r:
    print(0)
elif not max_c:
    print(min_r + max_r)
elif not max_r:
    print(min_c + max_c)
else:
    print(min_r + max_r + min_c + max_c)
