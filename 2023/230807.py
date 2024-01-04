def happyhappyhappy(x, y):
    global answer

    if x and sum(x) == m:
        answer += 1

    for i in range(y, n):
        happyhappyhappy(x + [nums[i]], i + 1)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
happyhappyhappy([], 0)
print(answer)