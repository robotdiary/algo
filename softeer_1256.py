# [인증평가(5차) 기출] 업무 처리
h, k, r = map(int, input().split())
# 노드의 개수 = 2 ** (h + 1) - 1
# 말단 직원의 수 = 2 ** h
nodes = [[] for i in range(2 ** (h + 1))]
for i in range(2 ** h):
    task = list(map(int, input().split()))
    for j in task:
        nodes[2 ** (h + 1) - (2 ** h) + i].append(j)

answer = 0
day = 2
while day <= r:
    for i in range(1, 2 ** (h + 1) - 1 - (2 ** h)):
        # 홀수일
        if day % 2:
            if len(nodes[i * 2]):
                nodes[i].append(nodes[i * 2].pop(0))
        else:
            if len(nodes[i * 2 + 1]):
                nodes[i].append(nodes[i * 2 + 1].pop(0))
        if i == 1:
            answer += nodes[1].pop(0)
    day += 1
    # print(nodes)

print(answer)