def bit_sum(list1):
    count = 0
    for i in range(1 << len(list1)):
        selected = []
        for j in range(len(list1)):
            if i & (1 << j):
                selected.append(list1[j])
        if sum(selected) == 0:
            count += 1
    if count > 1:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {bit_sum(list(map(int, input().split())))}')
