'''
10월 2일 오전 9시 23분 - 9시 39분 (16분)
'''
import math
# 바이러스 검사
N = int(input())
guests = list(map(int, input().split()))
a, b = map(int, input().split())
answer = 0
for i in range(N):
    if guests[i] <= a:
        answer += 1
        continue
    guest = guests[i] - a
    answer += math.ceil(guest / b) + 1

print(answer)
