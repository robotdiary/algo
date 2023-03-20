# 1, 2, 3 더하기
nums = [0] * 11
nums[1] = 1
nums[2] = 2
nums[3] = 4

for i in range(4, 11):
    nums[i] = sum(nums[i-3:i])

for _ in range(int(input())):
    print(nums[int(input())])
