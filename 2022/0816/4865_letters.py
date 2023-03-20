T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    answer = []
    for i in str1:
        count = str2.count(i)
        answer.append(count)
    print(f'#{tc} {max(answer)}')