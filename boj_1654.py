# 랜선 자르기
k, n = map(int, input().split())  # 가진 개수, 필요한 개수
lanlist = []
for _ in range(k):
    lanlist.append(int(input()))
left = 1
right = max(lanlist)

while left <= right:
    middle = (left + right) // 2  # 기준 점 = 가장 작은 밧줄
    ans = 0
    for i in lanlist:  # 각 밧줄을 가장 작은 밧줄로 나눈 몫이 n 이상이어야 함
        ans += i // middle  # 이하면 가장 작은 밧줄 += 반으로 나눔

    if ans >= n:
        left = middle + 1
    elif ans < n:
        right = middle - 1

print(right)