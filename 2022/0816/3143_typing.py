T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    for i in a:
        if b in a:
            a = a.replace(b, '1')
    print(f'#{tc} {len(a)}')