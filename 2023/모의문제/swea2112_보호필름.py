def test():
    for j in range(M):
        cnt = 1
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
                if cnt == K:
                    break
            else:
                cnt = 1
        else:
            return False
    return True


def cur(cnt, depth, start):
    global answer
    if depth == cnt:
        if test():
            answer = cnt
            return True
        return False

    for spec in range(start, N):
        a = ['1'] * M
        arr[spec], a = a, arr[spec]
        if cur(cnt, depth + 1, spec + 1):
            return True
        arr[spec], a = a, arr[spec]

        a = ['0'] * M
        arr[spec], a = a, arr[spec]
        if cur(cnt, depth + 1, spec + 1):
            return True
        arr[spec], a = a, arr[spec]
    return False


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())  # 두께, 가로크기, 합격기준
    arr = [list(input().split()) for _ in range(N)]  # 문자열

    if K == 1 or test():
        print(f'#{tc} 0')
    else:
        answer = 0
        for i in range(N):
            cur(i, 0, 0)
            if answer:
                break
        else:
            answer = -1
        print(f'#{tc} {answer}')