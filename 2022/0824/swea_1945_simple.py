# # 1945. 간단한 소인수분해 (D2)
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    answer = [0, 0, 0, 0, 0]
    while n > 1:
        if n % 11 == 0:
            n = n // 11
            answer[4] += 1
        elif n % 7 == 0:
            n = n // 7
            answer[3] += 1
        elif n % 5 == 0:
            n = n // 5
            answer[2] += 1
        elif n % 3 == 0:
            n = n // 3
            answer[1] += 1
        elif n % 2 == 0:
            n = n // 2
            answer[0] += 1

    print(f'#{tc}', *answer)

#  딕셔너리로 해봤는데 시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     answer = {'11': 0, '7': 0, '5': 0, '3': 0, '2': 0}
#     while n > 1:
#         for num in answer:
#             if n % int(num) == 0:
#                 n = n // int(num)
#                 answer[num] += 1
#     result = list(reversed(answer.values()))
#     print(f'#{tc}', *result)