# # 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5
# 3트 비율로 바꾸기
import sys
sys.stdin = open("input.txt", "r")

pwd = {
     '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
     '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9 }
ratio = {
    '1123': 0, '1222': 1, '2212': 2, '1141': 3, '2311': 4,
    '1321': 5, '4111': 6, '2131': 7, '3121': 8, '2113': 9
}

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    zero_line = '0' * m
    up = '0' * m
    arr = []
    for i in range(n):
        line = input()
        # 위와 동일한 문장이면 지나치기
        if line == up or line == zero_line:
            continue
        # 문장에서 암호문이 등장하면
        binary_code = ''
        if line:
            up = line
            # 문장 안을 돌면서
            for j in range(len(line)):
                # [1] 16진수를 만나면
                if line[j]:
                    # [2] 2진수로 변환하고 2진수 배열에 추가
                    binary_code += '0'*(4-len(str(bin(int(line[j], base=16)))[2:]))
                    binary_code += str(bin(int(line[j], base=16)))[2:]
                else:
                    binary_code += '0'
            arr.append(binary_code)

    # 끝위치 찾기
    row = end = 0
    stack = []
    visited = []
    ans = 0
    for N in range(len(arr)):
        M = len(arr[N])
        while M > 55:
            # 끝 점 찾기
            for i in range(M - 1, -1, -1):
                if arr[N][i] == '1':
                    row = N
                    end = i
                    break
            # 끝 점부터 개수 적기
            check = []
            cnt = 1
            i = end
            while len(check) < 33:
                # 끝에서부터 비율로 바꾸기
                if check and len(check) % 4 == 0 and 1 not in check[-4::]:
                    while 1 not in check[-4::]:
                        for i in range(-1, -5, -1):
                            check[i] = check[i] // 2
                if arr[N][i] == arr[N][i-1]:
                    cnt += 1
                    i -= 1
                else:
                    check.append(cnt)
                    cnt = 1
                    i -= 1
    # 유효성 검사
    #         check = check[::-1]
            code = ''
            codes = []
            for i in check:
                code += str(i)
            for i in range(0, len(check), 4):
                if code[i: i + 4] in ratio.keys():
                    codes.append(ratio[code[i: i + 4]])
                else:
                    codes = []
                    break
            if codes:
                odd = codes[0] + codes[2] + codes[4] + codes[6]
                even = codes[1] + codes[3] + codes[5] + codes[7]

                if (odd * 3 + even) % 10 == 0:
                    ans += odd + even

            M = i

    print(f'#{tc} {ans}')


# 2트
# import sys
# sys.stdin = open("input.txt", "r")
#
# pwd = {
#      '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
#      '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9 }
#
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     zero_line = '0' * m
#     up = '0' * m
#     arr = []
#     for i in range(n):
#         line = input()
#         # 위와 동일한 문장이면 지나치기
#         if line == up or line == zero_line:
#             continue
#         # 문장에서 암호문이 등장하면
#         binary_code = ''
#         if line:
#             up = line
#             # 문장 안을 돌면서
#             for j in range(len(line)):
#                 # [1] 16진수를 만나면
#                 if line[j]:
#                 # [2] 2진수로 변환하고 2진수 배열에 추가
#                     binary_code += '0'*(4-len(str(bin(int(line[j], base=16)))[2:]))
#                     binary_code += str(bin(int(line[j], base=16)))[2:]
#                 else:
#                     binary_code += '0'
#             arr.append(binary_code)
#     # 끝위치 찾기
#     stack = []
#     visited = []
#     row = end = 0
#     for N in range(len(arr)):
#         M = len(arr[N])
#         while M > 55 :
#             for i in range(M - 1, -1, -1):
#                 if arr[N][i] == '1':
#                     row = N
#                     end = i
#                     break
#             else:
#                 break
#             start = end - 56 + 1   # end - 55
#             if (start, end, row) not in visited:
#                 visited.append((start, end, row))
#                 stack.append((start, end, row))
#             M = start
#     # start 부터 7자리씩 잘라서 읽어오기
#     # 패턴의 모든 시작 위치를 생성
#     ans = 0
#     while stack:
#         start, end, row = stack.pop()
#         codes = []
#         for i in range(start, end, 7):
#             if arr[row][i: i + 7] in pwd.keys():
#                 codes.append(pwd[arr[row][i: i + 7]])
#             else:
#                 codes = []
#                 break
#         if codes:
#             odd = codes[0] + codes[2] + codes[4] + codes[6]
#             even = codes[1] + codes[3] + codes[5] + codes[7]
#
#             if (odd * 3 + even) % 10 == 0:
#                 ans += odd + even
#
#     print(f'#{tc} {ans}')


# # import sys
# # sys.stdin = open("input.txt", "r")
# # sys.stdout = open("output.txt", "w")
# # import strip
#
# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split()) # 세로, 가로
#     up = '0' * m
#     arr = []
#     for i in range(n):
#         line = input()
#         # 위와 동일한 문장이면 지나치기
#         if line == up:
#             continue
#         # 문장에서 암호문이 등장하면
#         binary_code = ''
#         if line:
#         #     print(i)
#         #     print(line)
#             up = line
#             # 문장 안을 돌면서
#             for j in range(len(line)):
#                 # [1] 16진수를 만나면
#                 if line[j]:
#                 # [2] 2진수로 변환하고 2진수 배열에 추가
#                     binary_code += '0'*(4-len(str(bin(int(line[j], base=16)))[2:]))
#                     binary_code += str(bin(int(line[j], base=16)))[2:]
#                 else:
#                     binary_code += '0'
#             arr.append(binary_code)
#     #         print(binary_code)
#     # print(arr)
#     ratio = {
#         '1123': 0, '1222': 1, '2212': 2, '1141': 3, '2311': 4,
#         '1321': 5, '4111': 6, '2131': 7, '3121': 8, '2113': 9
#     }
#     code = []
#     for i in range(len(arr)-2, -1, -1):
#         b = arr[i]
#         num = ''
#         # 이진수를 비율로 변환
#         print(b[::-1])
#         cnt = 1
#         # print(len(b))
#         # 56개에서 짜르기
#         idx = 1
#         for j in range(len(b)-1, 0, -1):
#             # print(j)
#             # if cnt >
#             if b[j] == b[j-1]:
#                 cnt += 1
#             else:
#                 if len(num) == 0 and cnt > 9:
#                     num += '0'
#                     cnt = 1
#                 else:
#                     num += str(cnt)
#                     cnt = 1
#         print(len(num))
#         print(num)
#             # [3] 비율을 암호 숫자로 변환
#     # for i in range(len(num)-1):
#
#             # 그리고 다음 숫자 확인하러? 코드로?
#
#             # [4] 모인 암호 숫자가 유효성을 통과하면
#
#             # [5] 답을 프린트하고 탈출
#
#             # [6] 유효성을 통과하지 못하면 하나 빼고 그 뒤에걸 확인
#             # [7] 인덱스가 끝나면 아래 줄로 내려가야 함