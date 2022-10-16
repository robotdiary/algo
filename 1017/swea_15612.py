# 15612. 체스판 위의 룩 배치 D3
for tc in range(1, int(input()) + 1):
    arr = [list(input()) for _ in range(8)]
    answer = 'yes'
    rook = [0]*8
    for line in arr:
        if line.count('O') == 1:
            if rook[line.index('O')]:
                answer = 'no'
                break
            else:
                rook[line.index('O')] = 1
        else:
            answer = 'no'
            break
    print(f'#{tc} {answer}')