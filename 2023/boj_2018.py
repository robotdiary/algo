# n = int(input())
# answer = 0
#
# for i in range(n):
#     target = 0
#     plus = n - i
#     while target < n and plus:
#         target += plus
#         plus -= 1
#     if n == target:
#         answer += 1
#
# print(answer)

n = int(input())
answer = 0
start = 0
end = 1
val = 1
while start <= end <= n:
    if val < n:
        end += 1
        val += end
    elif val == n:
        answer += 1
        start += 1
        val -= start
    else:
        start += 1
        val -= start

print(answer)