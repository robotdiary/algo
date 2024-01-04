# 범위 제곱근으로 / 출력 모아서 한번에로 바꿈
def 신비한소수찾기(num, depth):
    if depth == n:
        answer.append(num)
        return

    for i in [1, 3, 7, 9]:
        new_num = num * 10 + i
        for j in range(int(new_num ** 0.5), 2, -1):
            if not new_num % j:
                break
        else:
            신비한소수찾기(new_num, depth + 1)


n = int(input())
answer = []
for i in [2, 3, 5, 7]:
    신비한소수찾기(i, 1)

print(*answer, sep='\n')