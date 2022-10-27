# swea 14510. 나무 높이 D2
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    trees = list(map(int, input().split()))
    print(trees)
    day = 0
    pointer = 0
    while pointer <= len(trees):
