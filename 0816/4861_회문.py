T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    letters = [[0] * n for _ in range(n)]
    for i in range(n):
        letter = input()
        for j in range(n):
            letters[i][j] = letter[j]
    for i in range(n):
        for j in range(n-m+1):
            if letters[i][j:j+m//2] == letters[i][j+m-1:j+m//2-1:-1]:
                answer = ''.join(letters[i][j:j+m])
                print(f'#{tc} {answer}')
                break
    for i in range(n-m+1):
        for j in range(n): #
            if letters[i][j] == letters[i