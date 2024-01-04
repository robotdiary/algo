import heapq

for tc in range(int(input())):
    minq, maxq = [], []
    t = int(input())
    commands = list(tuple(input().split()) for _ in range(t))
    for char, char_num in commands:
        if char == 'I':
            heapq.heappush(minq, int(char_num))
            heapq.heappush(maxq, -int(char_num))
        elif char == 'D' and minq:
            if char_num == '1':
                minq.remove(-heapq.heappop(maxq))
            else:
                maxq.remove(-heapq.heappop(minq))
    if minq:
        print(-heapq.heappop(maxq), heapq.heappop(minq))
    else:
        print('EMPTY')