lst = list(int(input()) for _ in range(9))
target = sum(lst) - 100
for i in range(9):
    for j in range(i + 1, 9):
        if lst[i] + lst[j] == target:
            for p in range(9):
                if p not in {i, j}:
                    print(lst[p])
            exit(0)