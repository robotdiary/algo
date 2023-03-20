# 백준 11399 ATM
N = int(input())
P = list(map(int, input().split()))

P.sort()
answer = 0
acc = 0
for i in range(N):
    acc += P[i]
    answer += acc
print(answer)