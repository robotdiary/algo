def bina(idx):
    result = 0
    for i in range(n):
        result += int(yi[i]) * (2 ** (n - 1 - i))
    if int(yi[idx]):
        result -= 2 ** (n - 1 - idx)
    else:
        result += 2 ** (n - 1 - idx)
    return result


def mult(idx):
    acc = 0
    result = []
    for i in range(m):
        if i == idx:
            for k in range(2):
                result.append(s[sam[idx]][k] * (3 ** (m - 1 - idx)))
        else:
            acc += int(sam[i]) * (3 ** (m - 1 - i))
    return result[0] + acc, result[1] + acc


s = {'1': (2, 0), '2': (1, 0), '0': (1, 2)}
for tc in range(1, int(input()) + 1):
    yi = input()
    sam = input()
    n, m = len(yi), len(sam)
    flag = 0
    for i in range(n):
        y = bina(i)
        for j in range(m):
            one, two = mult(j)
            if y == one or y == two:
                print(f'#{tc} {y}')
                flag = 1
                break
        if flag:
            break