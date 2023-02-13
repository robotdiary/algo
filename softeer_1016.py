import sys
import heapq

heap = []

w, n = map(int, input().split())
for _ in range(n):
    weight, price = map(int, input().split())
    heapq.heappush(heap, (-price, weight))
answer = 0
while w and heap:
    price, weight = heapq.heappop(heap)
    print('전', weight, price, w)
    if w >= weight:
        w -= weight
        answer += weight * (price * -1)
    else:
        answer += w * (price * -1)
        w = 0
        break
    print('후', weight, answer, w)
print(answer)