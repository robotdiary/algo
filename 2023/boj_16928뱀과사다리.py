import heapq
n, m = map(int, input().split())
warf = dict()
for _ in range(n + m):
    k, v = map(int, input().split())
    warf[k] = v

answer = 17
q = [(0, 1)]
visited = {(0, 1)}
while q:
    cnt, current = heapq.heappop(q)
    # if current >= 100:
    #     answer = cnt
    #     break
    if current >= 94:
        answer = cnt + 1
        break

    no_warf = 0
    for destination in range(6, 0, -1):
        if warf.get(current + destination, 0):
            if (cnt + 1, warf[current + destination]) not in visited:
                heapq.heappush(q, (cnt + 1, warf[current + destination]))
                visited.add((cnt + 1, warf[current + destination]))
        else:
            # if current + destination <= 100:
            no_warf = max(destination, no_warf)
    if no_warf and (cnt + 1, current + no_warf) not in visited:
        heapq.heappush(q, (cnt + 1, current + no_warf))
        visited.add((cnt + 1, current + no_warf))

print(answer)