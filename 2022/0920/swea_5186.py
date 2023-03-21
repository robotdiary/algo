# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
T = int(input())
for tc in range(1, T + 1):
    num = float(input())   # 정수로 읽어야 함
    bin = ''
    for i in range(1, 13): # 1부터 12승을 구하는 것
        if num <= 0:       # 같음을 빼먹으면 안 된다.
            break
        if num >= 2 ** -i: # 클 때, 뺄 수 있음
            num -= 2 ** -i
            bin += '1'
        else:
            bin += '0'
        # print(num)
    if num:
        bin = 'overflow'
    print(f'#{tc} {bin}')

    # tc 8/10 통과
    # # 숫자가 0이 되거나 12자리까지 반복
    # while num > 0 and len(bin) < 13:
    #     if num >= 2 ** -i: # 같을 때를 빼먹었네!!!
    #         num -= (2 ** -i)
    #         bin += '1'
    #         i += 1
    #     else:
    #         i += 1
    #         bin += '0'
    # if i > 12:
    #     print(f'#{tc} overflow')
    # else:
    #     print(f'#{tc} {bin}')