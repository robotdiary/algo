# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
def dfs(s, e, depth):
    global answer
    # 깊이가 깊으면 answer이다.
    if depth > answer:
        answer = depth

    if (s, e) not in visited:
        visited.add((s, e))
    for i in range(len(time)):
        if time[i][0] >= e and time[i] not in visited: # 뒤 조건 안 걸면 time error
            dfs(time[i][0], time[i][1], depth+1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    time = [tuple(map(int, input().split())) for _ in range(n)]
    # 가장 빨리 끝나는 작업을 구한다.
    time.sort(key=lambda x: x[1])
    stack = list()
    visited = set()
    answer = 0
    # 가장 빨리 끝나는 작업부터 시작
    start, end = time[0]
    dfs(start, end, 1)

    print(f'#{tc} {answer}')
