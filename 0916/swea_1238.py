# 1238. [S/W 문제해결 기본] 10일차 - Contact D4
for tc in range(1, 11):
    length, start = map(int, input().split()) # 24
    contact = list(map(int, input().split())) # [0]~[23]
    parent = []
    child = [[] for i in range(length//2)]   # 12
    for i in range(length//2):  # 0, 1, 2,,, 11
        if contact[i*2] not in parent:
            parent.append(contact[i*2])
            child[parent.index(contact[i*2])].append(contact[i*2+1])
        elif contact[i * 2 + 1] not in child[parent.index(contact[i * 2])]:
            child[parent.index(contact[i * 2])].append(contact[i * 2 + 1])

    visited = set({})
    answer = 0
    q = [start]
    # depth = 0
    while q:
        size = len(q)
        max_num = []
        for i in range(size):
            current = q.pop(0)
            max_num.append(current)
            if current not in visited:
                visited.add(current)
                if current in parent:
                    for friend in child[parent.index(current)]:
                        if friend not in visited:
                            q.append(friend)
        answer = max(max_num)
        # depth += 1
    print(f'#{tc} {answer}')