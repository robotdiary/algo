T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    # ['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij']
    answer = ''
    for i in range(15):
        for j in range(5):
            try:
                answer = answer + words[j][i]
            except:
                pass
    print(f'#{tc} {answer}')