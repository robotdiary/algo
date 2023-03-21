# start 연습문제1
# [2] 내장모듈로 풀기
# T = int(input())
# for tc in range(1, T + 1):
#     nums = input()
#     answer = []
#     for i in range(0, len(nums), 7):
#         num = nums[i:i + 7]
#         ans = int(num, base=2)
#         answer.append(ans)
#     print(*answer)

# [1] 그냥 풀기
# T = int(input())
# for tc in range(1, T + 1):
#     nums = input()
#     answer = []
#     for i in range(0, len(nums), 7):
#         ans = 0
#         num = nums[i:i+7] # 문자열
#         for j in range(7):
#             if num[j] == '1':
#                 ans += 1<<(6-j)
#                 # print(1<<(6-j))
#                 # print(ans)
#         answer.append(ans)
#     print(*answer)
# print(1<<3)
# print(bin(8))