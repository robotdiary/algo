# 전혀 모르겠음 답을 외우자
'''
포함배제
포카드 홀수일때는 더하고 짝수일때는 빼고
벤다이어그램 겹치는거 빼는 느낌으로 생각하기
'''
from math import comb
n = int(input())
answer = 0
for i in range(1, 14):
    if n >= 4*i:
        if i % 2:
            answer = (answer + comb(52 - 4 * i, n - 4 * i) * comb(13, i)) % 10007
        else:
            answer = (answer - comb(52 - 4 * i, n - 4 * i) * comb(13, i)) % 10007
print(answer)

# 전혀 모르겠음
# def poker(x, y):
#     global answer
#
#     if not x:
#         return
#
#     for i in range(y, 53):
#         check[i % 13] += 1
#         if check[i % 13] == 4:
#             # 남은 횟수만큼 +하고 continue
#             cnt = 1
#             for j in range(1, x):
#                 cnt *= 52 - (i + j)
#             answer += cnt
#         else:
#             poker(x - 1, i + 1)
#         check[i % 13] -= 1
#
#
# n = int(input())
# if n < 4:
#     print(0)
# elif n > 51:
#     print(1)
# else:
#     answer = 0
#     check = [0] * 13
#     poker(n, 1)
#     print(answer)