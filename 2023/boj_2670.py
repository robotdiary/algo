# 연속 부분 최대곱
n = int(input())
nums = []
for _ in range(n):
    nums.append(float(input()))
# O(n**2)
answer = 0
for i in range(n):
    val = 1
    for j in range(i, n):
        val *= nums[j]
        if val > answer:
            answer = val
# print(round(answer, 3))  # 억까다
print(f'{answer:.3f}')

# print(round(2.5))  # 2
# print(round(3.5))  # 4

# # O(n)
# mul = 1.0
# for f in lst:
#     if mul<1.0:             # 새로운 숫자로 시작
#         mul = f
#     else:
#         mul *= f
#     ans = max(ans, mul)
