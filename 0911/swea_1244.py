# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
def dfs(l, c, n): # 3, 1
    global answer
    if c == 0:
        result = ''
        for z in n:
            result += z
            if result > answer:
                answer = result
        return
    elif answer == sort_n:

    for i in range(l-1): # 0, 1
        for j in range(i+1, l): # 1, 2 / 2
            if answer[i] > n[j]:
                continue
            else:
                n[i], n[j] = n[j], n[i]
                if n[i] < answer[i]:
                    continue
                else:
                    dfs(l, c-1, n)
                    if answer == sort_n and (c-1) % 2:
                        n[-1], n[-2] = n[-2], n[-1]
                        result = ''
                        for z in n:
                            result += z
                            answer = result
                        return
                    elif answer == sort_n:
                        result = ''
                        for z in n:
                            result += z
                            answer = result
                        return
                    n[i], n[j] = n[j], n[i]


T = int(input())
for tc in range(1, T + 1):
    num, cnt = input().split() # '123', '1'
    n = list(num) # ['1', '2', '3']
    sort_n = sorted(n, reverse=True)
    count = int(cnt) # 1
    answer = max(n) + '0'*(len(n)-1)
    dfs(len(n), count, n) # 3, 1
    print(f'#{tc} {answer}')

# a = ['1', '2', '3']
# print(max(a) + '0'*3)

# T = int(input())
# for tc in range(1, T + 1):
#     num, cnt = input().split() # '123', '1'
#     n = list(num) # ['1', '2', '3']
#     c = 0
#     check = 0
#     # [1] 내림차순으로 삽입정렬
#     for i in range(len(n) - 1): # 0, 1, 2, 3
#         # 정해진 교환 숫자에 다다르면 멈춤
#         if c >= int(cnt):
#             break
#         # 매번 교환하지 않고 최대 숫자와만 교환
#         maxi = '0'
#         # 최대수가 2개 이상일 때, 뒤에 있는 것과 교환
# 32888 2 에서 88823이 나옴 답은 88832
#         for j in range(len(n)-1, i, -1): # 4, 3
#             if n[j] > n[i] and n[j] > maxi:
#                 maxi = n[j]
#                 idx = j
#             if n[i] == n[j]: # 같은 숫자가 있는지 판별
#                 check = 1
#         if maxi != '0':
#             n[i], n[idx] = n[idx], n[i]
#             c += 1
#     else:
#         if not check and int(cnt) > c and (int(cnt) - c) % 2:
#             n[-1], n[-2] = n[-2], n[-1]
#
#     # 출력 형식
#     answer = ''
#     for z in n:
#         answer += z
#     print(f'#{tc} {answer}')