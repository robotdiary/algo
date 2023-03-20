# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 D3
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    ns = list(map(int, input().split()))
    ms = list(map(int, input().split()))
    ns.sort()
    answer = 0
    for i in ms:
        pattern = []
        l = 0
        r = len(ns)-1
        middle = (l + r) // 2
        while l <= r:
            if ns[middle] == i:
                answer += 1
                break
            elif i < ns[middle]:
                r = middle - 1
                middle = (l + r) // 2
                pattern.append('l')
                if len(pattern) > 1 and pattern[-1] == pattern[-2]:
                    break
            else:
                l = middle + 1
                middle = (l + r) // 2
                pattern.append('r')
                if len(pattern) > 1 and pattern[-1] == pattern[-2]:
                    break

    print(f'#{tc} {answer}')