# swea 14510. 나무 높이 D2
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    trees = list(map(int, input().split()))

    point = max(trees)
    day = 1
    pointer = 0
    # [1] 모든 나무가 커질 때까지 반복
    while pointer <= len(trees):
        # [2] 전체를 돌면서 물 주기
        for i in range(pointer, len(trees)):
            if day % 2:
                water = 1
            else:
                water = 2
            if point - trees[i] >= water:
                trees[i] += water
                day += 1