# 떡먹는 호랑이
D, K = map(int, input().split())
d = [0] * 31
d[1] = (1,0) # 첫째날 떡의 갯수 1a + b
d[2] = (0,1) # 둘째날 떡의 갯수 1b + 0a
for i in range(3, D+1): # D번째날 떡의 갯수
    d[i] = (d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1])

# D번째 날의 a와 b의 계수
a = d[D][0]
b = d[D][1]

n,m = 1,1 # a와 b의 값
# 브루트포스 알고리즘
while True:
    if a*n + b*m == K: # a와 b의 값을 찾았다면 출력
        print(n,m,sep='\n')
        break
    elif a*n + b*m < K: # a와 b값이 k 보다 작다면 b의 값을 하나키움
        m += 1
    else: # 값이 크다면 a 값 하나 키우고 b는 다시 1부터
        n += 1
        m = 1

# d, k = map(int, input().split())
# days = [[0, 0], [1, 0], [0, 1], [1, 1]]
# for day in range(4, 31):
#     days.append([days[day-1][0]+days[day-2][0], days[day-1][1]+days[day-2][1]])
# x, y = days[d]
# answer = [0, 0]
# flag = 1
# while flag:
#     if (k - (x*flag)) % y:
#         flag += 1
#         continue
#     else:
#         ans = (k - (x*flag)) // y
#         if flag <= ans:
#             answer = [flag * 1, ans * 1]
#             flag = 0
#             break
#         flag += 1
# print(*answer, end='\n')
