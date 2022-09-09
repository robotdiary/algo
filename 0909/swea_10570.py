import math
# 10570. 제곱 팰린드롬 수 D3
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    check = a # 10
    check_lst = list(str(a))
    cnt = 0
    while check <= b:
        if check_lst == list(reversed(check_lst)):
            a_sqrt = math.sqrt(check)
            if a_sqrt == int(a_sqrt):
                answer = list(str(int(a_sqrt)))
                if answer == list(reversed(answer)):
                    cnt += 1
        check += 1
        check_lst = list(str(check))
    print(f'#{tc} {cnt}')

# a = ['1', '2', '3']
# b = ''.join(a)
# a = list('123')
# print(a)
# a = 3.14
# a, b = map(list, input().split())
# print(int(a))
# print(1 == 1.0)