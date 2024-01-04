n = int(input())  # 1~100
ice = [tuple(map(int, input().split())) for _ in range(n)]
ice.sort(key=lambda x:x[1])
answer = 0

left = 0
idx = 1
while left < n:
    while idx < n and ice[idx][0] <= ice[left][1]:
        idx += 1
    answer += 1
    left = idx
    idx += 1

print(answer)