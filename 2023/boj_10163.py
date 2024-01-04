arr = [0] * 1001 ** 2
n = int(input())
for tc in range(n):
    xc, xr, w, h = map(int, input().split())
    for i in range(h):
        arr[(xr + i) * 1001 + xc:(xr + i) * 1001 + xc + w] = [tc+1] * w
for i in range(n):
    print(arr.count(i+1))