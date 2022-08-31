T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    letters = [[0] * n for _ in range(n)]
    for i in range(n):
        letter = input()
        for j in range(n):
            letters[i][j] = letter[j]
    result = 1
    for i in range(n): # n = 20, m = 13, 인덱스 7 - 19
        for j in range(n-m+1): # j = 7-13, 19-13
            if m % 2 == 0 and letters[i][j:j+m//2] == letters[i][j+m-1:j+m//2-1:-1]:
                answer = ''.join(letters[i][j:j+m])
                print(f'#{tc} {answer}')
                result -= 1
                break
            elif m % 2 and letters[i][j:j+m//2] == letters[i][j+m-1:j+m//2:-1]:
                answer = ''.join(letters[i][j:j+m])
                print(f'#{tc} {answer}')
                result -= 1
                break
    if result:
        column = list(map(list, zip(*letters)))
        for i in range(n):  # n = 20, m = 13, 인덱스 7 - 19
            for j in range(n - m + 1):  # j = 7-13, 19-13
                if m % 2 == 0 and column[i][j:j + m // 2] == column[i][j + m - 1:j + m // 2 - 1:-1]:
                    answer = ''.join(column[i][j:j + m])
                    print(f'#{tc} {answer}')
                    result -= 1
                    break
                elif m % 2 and column[i][j:j + m // 2] == column[i][j + m - 1:j + m // 2:-1]:
                    answer = ''.join(column[i][j:j + m])
                    print(f'#{tc} {answer}')
                    result -= 1
                    break