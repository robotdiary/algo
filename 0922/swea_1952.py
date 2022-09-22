# 1952. [모의 SW 역량테스트] 수영장
# [2] 재귀로 풀기
# def swimplan(month, acc):
#     global answer
#     if acc > answer:
#         return
#     if month >= 12:
#         if acc < answer:
#             answer = acc
#         return
#     swimplan(month + 1, acc + arr[month])
#     swimplan(month + 3, acc + quarter)
#
#
# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     cal = list(map(int, input().split()))
#     arr = [0] * 12
#     for i in range(12):
#         if cal[i] * day < month:
#             arr[i] = cal[i] * day
#         else:
#             arr[i] = month
#     answer = min(sum(arr), year)
#     swimplan(0, 0)
#     print(f'#{tc} {answer}')

# [1] 120분동안 도전! 10분 전에 성공~
# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     cal = list(map(int, input().split()))
#     answer = 0
#     arr = [0]*12
#     for i in range(12):
#         if cal[i] * day < month:
#             arr[i] = cal[i] * day
#         else:
#             arr[i] = month
#     answer = sum(arr)
#     # 3개월 연속 갈 때 계산
#     triplet = [20000] * 12
#     plus = 0
#     for f in range(5):
#         for i in range(12):
#             # 1번만 연속할 때
#             if i == 11:
#                 if quarter < arr[11]:
#                     triplet[11] = answer - arr[11] + quarter
#             elif i == 10:
#                 if arr[10] + arr[11] > quarter:
#                     triplet[10] = answer - (arr[10] + arr[11]) + quarter
#             elif cal[i+2] and cal[i] and cal[i+1]:
#                 if quarter < arr[i+2] + arr[i] + arr[i+1]:
#                     triplet[i] = answer - (arr[i+2] + arr[i] + arr[i+1]) + quarter
#         if min(triplet) < answer:
#             answer = min(triplet)
#             zero = triplet.index(min(triplet))
#             if zero < 11:
#                 arr[zero] = arr[zero+1] = arr[zero+2] = 0
#             elif zero == 11:
#                 arr[zero] = arr[zero+1] = 0
#             else:
#                 arr[zero] = 0
#             triplet = [20000] * 12
#         else:
#             break
#     if answer > year:
#         answer = year
#     if quarter * 4 < answer:
#         answer = quarter * 4
#     print(f'#{tc} {answer}')


