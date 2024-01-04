def perm(depth, acc):
    global mx, mn
    if depth == n - 1:
        mx = max(mx, acc)
        mn = min(mn, acc)

    for op in range(4):
        if operations[op]:
            operations[op] -= 1
            perm(depth + 1, calculator(acc, a[depth + 1], op))
            operations[op] += 1


def calculator(num1, num2, operater):
    if operater == 0:
        return num1 + num2
    elif operater == 1:
        return num1 - num2
    elif operater == 2:
        return num1 * num2
    else:
        if num1 < 0 < num2:
            return -(-num1 // num2)
        return num1 // num2


n = int(input())  # 수의 개수
a = list(map(int, input().split()))  # 수열
operations = list(map(int, input().split()))  # 연산자 수
mx, mn = -9999999999, 9999999999
perm(0, a[0])
print(mx)
print(mn)