table = [[0] * 100 for _ in range(100)]
for tc in range(1, 11):
    t = int(input())
    # 1은 N극 아래로감, 2는 S극 위로감
    for i in range(100):
        table[i] = list(map(int, input().split()))
# 스택
    zip_table = list(map(list, zip(*table)))
    cnt = 0
    for i in range(100):
        stack = [] # 줄마다 새로 담기
        for j in range(100):
# 2 나왔을 때 스택에 담았다가 1 없으면 버리고 1 있으면
            if zip_table[i][j] == 1 and stack:
                pass
            elif zip_table[i][j] == 1:
                stack.append(1)
# 1 나왔을 때 스택에 2 없으면 버리고 있으면 pop(), cnt += 1
            elif zip_table[i][j] == 2 and stack:
                cnt += 1
                stack.pop()
    print(f'#{tc} {cnt}')

# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# table[0] = list(map(int, input().split()))
# print(table)
# stack = []
# print(stack.pop()) # indexError