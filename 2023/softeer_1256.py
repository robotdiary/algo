# [인증평가(5차) 기출] 업무 처리
h, k, r = map(int, input().split())  # 높이, 업무 수, 날짜
# 노드의 개수 = 2 ** (h + 1) - 1
high = [2 * x for x in range(h + 1)]
works = 0
nodes = [[] for i in range(2 ** (h + 1))]
for i in range(high[-1]):
    work = list(map(int, input().split()))
    nodes[2 ** (h + 1) - high[h] + i] += work
    works += sum(work)
answer = 0
day = 2
while 1 < day <= r:
    # print(nodes[1], works)
    if sum(nodes[1]) == works:
        break
    for i in range(1, 2 ** (h + 1) - high[h]):
        # 홀수일
        if day % 2:
            if nodes[i * 2]:
                nodes[i].append(nodes[i * 2].pop(0))
        # 짝수일
        else:
            if nodes[i * 2 + 1]:
                nodes[i].append(nodes[i * 2 + 1].pop(0))
    day += 1

    # print(nodes)
print(sum(nodes[1]))