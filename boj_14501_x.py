# # 퇴사
# def work(day):
#     answer


# N = int(input())  # 1-15
# schedule = []
# for i in range(N):
#     schedule.append((map(int, input().split())))
# answer = 0
# for i, j in schedule:
#     work(i, j)
# print(answer)
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
dp =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):     
    if T[i]+i <= n:      
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])   
    else:                
        dp[i] = dp[i+1]
print(dp[0])