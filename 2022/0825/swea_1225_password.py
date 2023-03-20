# 1225 암호생성기
for _ in range(10):
    tc = int(input())
    num = list(map(int, input().split()))
    while num[-1]:
        for i in range(1, 6):
            n = num.pop(0)
            n -= i
            num.append(n)
            if num[-1] < 1:
                num[-1] = 0
                break
    print(f'#{tc}', *num)

