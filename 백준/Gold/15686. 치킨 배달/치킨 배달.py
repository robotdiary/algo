def find_city_distance(lst):
    global answer
    city = 0
    for hr, hc in homes:
        # 집으로부터 가장 가까운 치킨집을 찾고
        distance = 987654321
        for cr, cc in lst:
            distance = min(distance, abs(cr - hr) + abs(cc - hc))
        # 도시의 치킨거리에 더하는데
        city += distance
        # 이미 너무 멀면 gg
        if city >= answer:
            return
    answer = city


def fine_chicken():
    for i in range(1 << chicken):
        pick = []
        for j in range(chicken):
            if i & (1 << j):
                pick.append(chickens[j])
        if len(pick) <= m:
            find_city_distance(pick)


n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
homes = []
chickens = []
chicken = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == '1':
            homes.append((r, c))
        elif arr[r][c] == '2':
            chickens.append((r, c))
            chicken += 1
answer = 987654321
fine_chicken()
print(answer)