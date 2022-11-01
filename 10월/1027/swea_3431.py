# 3431. 준환이의 운동관리 D3
T = int(input())
for tc in range(1, T + 1):
    l, u, x = map(int, input().split())
    if x > u:
        print(f'#{tc} -1')
    elif x < l:
        print(f'#{tc} {l-x}')
    else:
        print(f'#{tc} 0')