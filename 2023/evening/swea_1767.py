# 1767. [SW Test 샘플문제] 프로세서 연결하기
def find_line(link, line, depth, visited):
    global answer
    if depth == len(core):
        if link > answer[0]:
            answer = [link, line]
        elif link == answer[0] and line < answer[1]:
            answer[1] = line
        return

    for d in range(4):
        visit = set()
        ll = 0
        nr, nc = core[depth][0] + di[d], core[depth][1] + dj[d]
        while 0 <= nr < n and 0 <= nc < n:
            if (nr, nc) not in visited and not arr[nr][nc]:
                visit.add((nr, nc))
                ll += 1
                nr += di[d]
                nc += dj[d]
            else:
                # 남은 코어 수가 적으면 돌 필요 X
                if answer[0] <= link + (len(core)-depth+1):
                    find_line(link, line, depth + 1, visited)
                break
        else:
            if answer[0] <= link + (len(core) - depth + 1):
                find_line(link + 1, line + ll, depth + 1, visited | visit)


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 0 = 빈, 1 = core
    answer = [0, 999999999]  # [코어 수, 전선 수]

    # 코어의 위치를 미리 다 찾아놓음
    core = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j] == 1:
                core.append((i, j))

    find_line(0, 0, 0, set())

    if answer[1] == 999999999:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {answer[1]}')

