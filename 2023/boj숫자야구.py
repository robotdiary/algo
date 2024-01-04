def perm():
    lst = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    lst.append((str(100 * i + 10 * j + k)))
    return lst


def baseball_game(x, st, ba):
    idx = 0
    while p and idx < len(p):
        strike = 0
        ball = 0
        num = p[idx]
        for char in range(3):
            if num[char] == x[char]:
                strike += 1
            elif num[char] in x:
                ball += 1
        if (st, ba) != (strike, ball):
            p.remove(num)
        else:
            idx += 1


n = int(input())
p = perm()

for _ in range(n):
    nums, s, b = input().split()
    baseball_game(nums, int(s), int(b))
print(len(p))