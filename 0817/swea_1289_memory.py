# 1289 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T + 1):
    memory = input()
    cnt = 0
    check = '0'
    for i in memory:
        if i != check:
            cnt += 1
            check = i
    print(f'#{tc} {cnt}')