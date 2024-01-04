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


def find_chicken_comb():  # m개 이하의 치킨집 조합 찾기
    for i in range(1 << chicken):
        pick = []
        for j in range(chicken):
            if i & (1 << j):
                pick.append(chickens[j])
        if len(pick) <= m:
            find_city_distance(pick)


n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
homes = []  # 집좌표모음.zip
chickens = []  # 치킨의 좌표
chicken = 0  # 총 치킨집 수
for r in range(n):
    for c in range(n):
        if arr[r][c] == '1':
            homes.append((r, c))
        elif arr[r][c] == '2':
            chickens.append((r, c))
            chicken += 1
answer = 987654321
find_chicken_comb()
print(answer)