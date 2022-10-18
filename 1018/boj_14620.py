# 백준 14620 꽃길 (S)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [(n, n) for _ in range(3)]
# print(visited)
answer = [987654321]*3  # 꽃 3개
for ans in range(3):
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (i, j) not in visited[0] and (i, j) not in visited[1]:
                visit = [(i, j)]
                price = arr[i][j]
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if (i + dr, j + dc) not in visited[0] and (i + dr, j + dc) not in visited[1]:
                        price += arr[i+dr][j+dc]
                        visit.append((i + dr, j + dc))
                    else:
                        break
                else:
                    if price < answer[ans]:
                        answer[ans] = price
                        visited[ans] = visit
# print(visited)
# print(answer)
print(sum(answer))