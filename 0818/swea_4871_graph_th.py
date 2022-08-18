T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split()) # 6 5
    e_lst = [list(map(int, input().split())) for _ in range(e)]
    # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    s, g = map(int, input().split())

    stack = [s]
    visited = []
    result = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        if current == g:
            result = 1
            break
        for i in e_lst:
            if i[0] == current:
                stack.append(i[1])
    print(f'#{tc} {result}')