for tc in range(1, int(input()) + 1):
    n = int(input())
    trees = list(map(int, input().split()))
    mx = max(trees)

    sm = 0
    day = 0
    # [1] 자라야 할 양과 홀수 만큼 커야 하는 나무 세기
    for i in range(n):
        trees[i] = mx - trees[i]
        sm += trees[i]
