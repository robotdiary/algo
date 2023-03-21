# 2105. [모의 SW 역량테스트] 디저트 카페
def left(r, c, depth, visited, cnt):
    for jump in range(depth):
        r += 1
        c -= 1
        if 0 <= r < n and 0 <= c < n and arr[r][c] not in visited:
            visited.add(arr[r][c])
            cnt += 1
        else:
            return

    while 0 <= r < n and 0 <= c < n:
        right(r, c)



def right(r, c):
    r += 1
    c += 1


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = -1
    # 전체 탐색
    for i in range(1, n-1):
        for j in range(1, n-2):
            left(i, j, {arr[i][j]}, 0)
    print(f'#{tc} {answer}')