# 1211 ladder2
T = 10
for tc in range(1, T+1):
    t = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    answer = 99999
    result = -1
    for i in range(100): # 모든 시작점 검사
        if ladder[0][i] == 1:
            visited = [] # 답이 될 방문 리스트
            go = 1 # 플래그
            r, c = (1, i) # 현재 위치
            while go:
                visited.append((r, c))
                for nr, nc in [(0, -1), (0, 1), (1, 0)]: #좌, 우, 위
                    if r+nr == 99 and ladder[r+nr][c+nc] == 1:
                        if len(visited) < answer:
                            answer = len(visited)
                            result = i
                            go = 0
                            break
                        else:
                            go = 0
                            break
                    elif 0 <= c+nc < 100 and ladder[r+nr][c+nc] == 1 and (r+nr, c+nc) not in visited:
                        visited.append((r+nr, c+nc))
                        r, c = r+nr, c+nc

    print(f'#{t} {result}')