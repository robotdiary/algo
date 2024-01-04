# 가장 빠른 문자열 타이핑
for tc in range(1, int(input()) + 1):
    a, b = input().split()
    cnt = a.count(b)
    print(f'#{tc} {len(a) - (cnt * len(b)) + cnt}')