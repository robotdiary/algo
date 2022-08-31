T = int(input())
for tc in range(1, T+1):
    line = int(input())
    triangle = [[1]*i for i in range(1, line+1)]
    for i in range(2, line):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
    print(f'#{tc}')
    for answer in range(line):
        print(*triangle[answer])