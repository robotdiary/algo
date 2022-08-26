# 2805 농작물 수확하기
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]
    answer = 0
    for i in range(n//2+1):
        if i == n//2:
            answer += sum(field[i])
        else:
            answer += sum(field[i][n//2-i:n//2+1+i])
            answer += sum(field[n-1-i][n//2-i:n//2+1+i])

    print(f'#{tc} {answer}')