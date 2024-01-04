from collections import defaultdict
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = (987654321, 0)  # 시간, 높이
height = defaultdict(int)

for i in range(n):
    for j in range(m):
        height[arr[i][j]] += 1

for i in range(min(height.keys()), max(height.keys()) + 1):
    low, high = 0, 0
    for j in height.keys():
        if i < j:
            high += height[j] * (j - i)
        elif i > j:
            low += height[j] * (i - j)

    if low <= high + b:
        time = high * 2 + low
        if time < answer[0]:
            answer = (time, i)
        elif time == answer[0]:
            answer = (time, max(i, answer[1]))

if answer[0] == 987654321:  #??여길 고쳤지만 의미 없는 것 같다
    print(0, arr[0][0])
else:
    print(*answer)
