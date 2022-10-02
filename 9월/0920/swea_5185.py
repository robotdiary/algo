# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
T = int(input())
for tc in range(1, T + 1):
    n, hexa = input().split()
    hexa = list(hexa)
    # print(n)
    # print(hexa)
    answer = ''
    for i in range(int(n)):
        num = int(hexa[i], base=16)
        if len(str(bin(num))[2:]) < 4:
            answer += '0'*(4-len(str(bin(num))[2:]))
            answer += str(bin(num))[2:]
        else:
            answer += (str(bin(num))[2:])
    print(f'#{tc} {answer}')

# print(bin(4))
# print(bin(7))
# print(bin(15))
# print(bin(14))