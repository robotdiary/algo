# 1949. [모의 SW 역량테스트] 등산로 조성
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split()) # 지도, k
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    peaks = 0
    s = []
    # 가장 높은 봉우리 찾기
    for i in range(n):
        if max(arr[i]) > peaks:
            peaks = max(arr[i])
    # 봉우리 좌표를 stack에 넣고 꺼내면서 DFS
    for i in range(n):
        for j in range(n):
            if arr[i][j] == peaks:
                s.append((i, j, 1))
    for i in range(n):
        for j in range(n):
            for z in range(k+1):
                arr[i][j] = arr[i][j] - z
                for p in s:
                    stack = [p]
                    answer = 0
                    while stack:
                        current = stack.pop()
                        if current[2] > answer:
                            answer = current[2]
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            # 범위 안이면
                            if 0 <= current[0]+dr < n and 0 <= current[1]+dc < n:
                            # 갈 수 있는 낮은 길이면
                                if arr[current[0]][current[1]] > arr[current[0]+dr][current[1]+dc]:
                                    stack.append((current[0]+dr, current[1]+dc, current[2]+1))
                    if answer > result:
                        result = answer
                arr[i][j] = arr[i][j] + z
    print(f'#{tc} {result}')
