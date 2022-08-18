for _ in range(10):
    # [1] 자료 구조화 하기
    tc, e = map(int, input().split())
    stack = [0]
    e_lst = list(map(int, input().split()))
    visited = []
    result = 0
    # 스택
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        if current == 99:
            result = 1
            break
        for i in range(e):
            if e_lst[i * 2] == current:
                stack.append(e_lst[i * 2 + 1])
    print(f'#{tc} {result}')

