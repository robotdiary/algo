# 백준 14620 꽃길 (S)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flower = set()  # 모든 꽃이 있는 장소 저장
visit = []  # 한 개의 꽃이 있는 장소만 저장
answer = [987654321]*3
for count in range(3):
    for i in range(1, n-1):

        for j in range(1, n-1):
            price = arr[i][j]
            visited = [(i, j)]
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (i + dr, j + dc) not in flower:
                    price += arr[i + dr][j + dc]
                    visited.append((i + dr, j + dc))
                else:
                    break
            else:
                if price < answer[count]:
                    answer[count] = price
                    visit = visited
    for i in visit:
        flower.add(i)
print(sum(answer))