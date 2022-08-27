# 1289 원재의 메모리 복구하기(D3)
T = int(input())
for tc in range(1, T + 1):
    memory = map(int, input())
    check = 0
    cnt = 0
    for i in memory:
        if i != check:
            cnt += 1
            check = i
    print(f'#{tc} {cnt}')