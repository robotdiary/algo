for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # dfs (가능한 한 길만 쭉 찾는)
    stack = [(99, arr[-1].index(2))]
    visited = {(99, arr[-1].index(2))}
    while stack:
        cr, cc = stack.pop()
        for dr, dc in [(0, 1), (0, -1), (-1, 0)]:  # 우, 좌, 상
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 100 and 0 <= nc < 100 and (nr, nc) not in visited and arr[nr][nc]:
                # 맨 윗줄 (r == 0)에 도달하면 답 출력 / for만 탈출해도 stack이 비어서 while문을 돌지 않음
                if nr == 0:
                    print(f'#{tc} {cc}')
                    break
                stack.append((nr, nc))
                visited.add((nr, nc))
                break  # 한 번만 스택에 넣으면 for문을 더 돌면서 다른 방향을 확인하지 않아도 됨
