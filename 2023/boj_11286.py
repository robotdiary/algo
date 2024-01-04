# 절댓값 힙
import heapq
heap = []
heapq.heapify(heap)
for tc in range(int(input())):
    num = int(input())
    # 숫자가 입력되면 힙에 추가
    if num:
        if num < 0:
            heapq.heappush(heap, (-num, num))
        else:
            heapq.heappush(heap, (num, num))
    # 입력된 숫자가 0이라면 출력
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)