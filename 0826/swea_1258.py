# 1258 행렬찾기
def rc_square(sr, sc): # 0, 0
    global visited
    w = 0
    h = 0
    nr = sr # 0
     # 4
    # 아래가 0일 때까지
    while nr < n and arr[nr][sc]:
        nc = sc
        # 옆이 0일 때까지
        while nc < n and arr[nr][nc]: # 위치가 숫자면
            visited.append((nr, nc)) # 방문기록하고
            w += 1 # 가로길이 1 더하고
            nc += 1 # 옆 칸 확인하러 가라
        h += 1
        nr += 1
    return (h, w // h)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    cnt = 0
    result = [] # [(3, 4), (4, 5), (2, 3)]
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and arr[i][j]:
                result.append(rc_square(i, j))#함수 실행
                cnt += 1 # 네모의 개수
# 출력 형식 맞추기
# 곱의 크기가 작은 순서대로, 같으면 행이 작은 순서대로
    sort_result = sorted(result, key=lambda x: x[0] * x[1])
    for i in range(len(result)-1, 0, -1):
        for j in range(0, i):
            if sort_result[j][0] > sort_result[j+1][0] and sort_result[j][0] * sort_result[j][1] == sort_result[j+1][0] * sort_result[j+1][1]:
                sort_result[j], sort_result[j+1] = sort_result[j+1], sort_result[j]
    answer = []
    for i in range(len(sort_result)):
        answer.append(sort_result[i][0])
        answer.append(sort_result[i][1])
    print(f'#{tc} {cnt}', *answer)