# 나무높이
for tc in range(1, int(input()) + 1):
    n = int(input())
    a = list(map(int, input().split()))

    # 최대 나무까지 얼마나 커야하는지 측정
    tree = max(a)
    for i in range(n):
        a[i] = tree - a[i]
    answer = 0
    print(a)
    # 이틀 걸려 3씩 줄인다
    for i in range(n):
        answer += a[i] // 3 * 2
        a[i] = a[i] % 3
    print(a)
    print(answer)
    # 남은 1과 2의 개수를 센다
    one = 0
    two = 0
    for i in range(n):
        if a[i] == 1:
            one += 1
        elif a[i] == 2:
            two += 1
    # 같게 남은 건 이틀로 없애고
    # 많이 남은 녀석에 맞춰 물 준다
    if one == two:
        answer += one * 2
    elif one < two:
        answer += one * 2
        two -= one
        answer += two * 2
    else:
        answer += two * 2
        one -= two
        answer += 1
        one -= 1
        while one:
            answer += 2
            one -= 1

    print(f'#{tc} {answer}')
