'''
2시 50분 - 57분
상습적 노리턴
'''


def cur(depth, acc):
    global answer
    if depth == N:
        answer = max(answer, acc)
        return  # 상습범

    # 일 함
    if depth + a[depth][0] <= N:
        cur(depth + a[depth][0], acc + a[depth][1])
    # 일 안 함
    cur(depth + 1, acc)


N = int(input())
a = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0
cur(0, 0)
print(answer)