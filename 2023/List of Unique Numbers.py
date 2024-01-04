n = int(input())
lst = list(map(int, input().split()))

answer = 0
left, right = 0, 0
set_a = set()
cnt = 0
while right <= n:
    if set_a & {lst[right]}:
        left += 1
        set_a = set()
    else:
        cnt += 1
        right += 1
        set_a.add(lst[right])
# 남은 left 답에 추가해줘