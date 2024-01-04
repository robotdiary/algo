def solution(a):  # string '987'
    a_list = list(map(int, a))  # [9, 8, 7]
    answer = ""
    check = len(a_list)         # 3
    start, end = len(a_list)-1, -1  # 2, 0
    x, y = -1, -1
    while start - 1 > end:
        for j in range(start - 1, end, -1):
            if a_list[start] > a_list[j]:
                if x > 0 and end == j and a_list[start] > a_list[x]:
                    y, end = j, j
                    break
                x, y = start, j
                end = j
                break
        start -= 1
    if x == -1:
        return 'BIGGEST'

    a_list[x], a_list[y] = a_list[y], a_list[x]
    b_list = a_list[:y + 1] + sorted(a_list[y + 1:])
    for char in b_list:
        answer += str(char)
    return answer


n = int(input())  # '987'
for _ in range(n):
    print(solution(input()))
