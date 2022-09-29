# # 백준 9372 상근이의 여행
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # 국가 수, 비행기 수
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)
    stack = [1]
    visited = set()
    cnt = 0
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.add(now)
        #     cnt += 1
        # if len(visited) == n:
        #     break
        for next in arr[now]:
            if next not in visited:
                print(next)
                print(visited)
                cnt += 1
                stack.append(next)
    print(cnt)
