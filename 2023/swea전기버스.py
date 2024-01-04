from collections import deque
for tc in range(1, int(input()) + 1):
    n = list(map(int, input().split()))
    # 0: 정류장 수 / 1번 정류장 시작 / n-1번 정류장 끝
    q = deque([(1, n[1])])  # 1번에 n[1]만큼 충전
    visited = {(1, n[1])}
    depth = 0
    while q:
        for d in range(len(q)):
            current, battery = q.popleft()
            if current + battery >= n[0]:
                print(f'#{tc} {depth}')
                depth = -1
                break
            for i in range(1, battery + 1):
                if (current + i, n[current + i]) not in visited:
                    q.append((current + i, n[current + i]))
                    visited.add((current + i, n[current + i]))
        else:
            depth += 1

        if depth < 0:
            break
    else:
        depth = -1
        print(f'#{tc} {depth}')

# import heapq
# for tc in range(1, int(input()) + 1):
#     n = list(map(int, input().split()))
#     # 0: 정류장 수 / 1번 정류장 시작 / n-1번 정류장 끝
#     q = [(-n[1], 0, 1)]  # n[1]만큼 충전, 0번, 위치
#     while q:
#         battery, depth, current = heapq.heappop(q)
#         battery = -battery
#         if current + battery >= n[0]:
#             print(f'#{tc} {depth}')
#             break
#         for i in range(1, battery + 1):
#             heapq.heappush(q, (-n[current + i], depth + 1, current + i))
#     else:
#         print(f'#{tc} {-1}')
