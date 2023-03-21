# 1928. Base64 Decoder D2
# import base64
alpa = {
    'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'w': 48, 'x': 49, 'y': 50, 'z': 51
}
for tc in range(1, int(input()) + 1):
    encoding = input()
#     ans = base64.b64decode(data)  # b'Life itself is a quotation.'
#     answer = ans.decode('ascii')  # Life itself is a quotation.
#     print(f'#{tc} {answer}')
    data = []
    for i in encoding:
        if i in alpa.keys():
            data.append(alpa[i])
        elif i.isupper():
            data.append(int(i, base=32) - 10)
        elif i.islower():
            data.append(int(i, base=32) + 16)
        elif i.isdigit():
            data.append(int(i) + 52)
        elif i == '+':
            data.append(62)
        else:
            data.append(63)
    bit = ''
    for i in data:
        if len(bin(i)[2:]) == 6:
            bit += str(bin(i)[2:])
        else:
            bit += '0'*(6-len(bin(i)[2:]))
            bit += str(bin(i)[2:])
    answer = ''
    for i in range(0, len(bit), 8):
        answer += chr(int(bit[i:i+8], base=2))
    print(f'#{tc} {answer}')
