def sm(x, y):
    return int(x) + int(y)


def minus(x, y):
    return int(x) - int(y)


def supply(x, y):
    return int(x) * int(y)


def cur(start, acc):
    global answer
    # 종료 조건
    if start > N - 2:
        answer = max(answer, acc)
        return

    for i in range(start, N, 2):
        new_temp = acc
        n = start
        while n < i:
            new_temp += a[n]
            if a[n] == '+':
                sm(acc, a[n+1])
            elif a[n] == '-':
                minus(acc, a[n+1])
            else:
                supply(acc, a[n+1])

            n += 2
        if n == N:
            answer = max(answer, acc)
            continue
        if n == N - 3:
            new_temp += '(' + a[n] + a[n+1] + a[n+2] + ')'
            answer = max(answer, eval(new_temp))
            print(new_temp)
            continue
            
        if a[n+1] == '+':
            sm(acc, a[i+1])
        elif a[n] == '-':
            minus(acc, a[i+1])
        else:
            supply(acc, a[i+1])
        cur(i + 4, acc)


N = int(input())
a = input()

answer = 0
cur(0, 0)
print(answer)
