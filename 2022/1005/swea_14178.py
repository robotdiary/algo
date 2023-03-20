# swea 14178. 1차원 정원 D3
for tc in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    d = d * 2 + 1
    if n % d:
        print(f'#{tc} {n // d + 1}')
    else:
        print(f'#{tc} {n // d}')
