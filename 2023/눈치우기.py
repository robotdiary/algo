# 1시 15분 - 35분
import heapq

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = -a[i]
time = 0
heapq.heapify(a)
while len(a) > 1:
    first = -heapq.heappop(a)
    second = -heapq.heappop(a)
    time += second
    if time > 1440:
        break
    if first - second:
        heapq.heappush(a, -(first - second))
if a:
    time += -a[0]
if time > 1440:
    time = -1

print(time)