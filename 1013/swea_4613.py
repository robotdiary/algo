# 4613. 러시아 국기 같은 깃발 D4
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    # 줄마다 색을 맞추기 위해 색칠해야 할 개수
    # [[흰색], [파랑], [빨강]]
    perm = [[0]*n for _ in range(3)]
    for i in range(n):
        perm[0][i] = arr[i].count('B') + arr[i].count('R')
        perm[1][i] = arr[i].count('W') + arr[i].count('R')
        perm[2][i] = arr[i].count('B') + arr[i].count('W')

    # 개수의 합 중에서 가장 작은 것 찾기
    # 하양과 파랑은 무조건 한 줄은 있어야 하므로 1부터, 빨강은 0부터
    answer = 987654321
    for i in range(1, n-1):
        white = sum(perm[0][0:i])
        for j in range(1, n):                       # 1, 2, 3, 4
            blue = sum(perm[1][i:i+j])              # 하양의 뒤부터
            for z in range(n-1):                    # 0, 1, 2, 3
                if i + j + z == n - 1:              # 합이 n-1일 때만 확인
                    red = sum(perm[2][i+j:i+j+z])   # 파랑의 뒤부터
                    if white + blue + red < answer: # 최소일 때
                        answer = white + blue + red # 업데이트

    # 막줄은 무조건 빨강
    answer += perm[-1][-1]
    print(f'#{tc} {answer}')