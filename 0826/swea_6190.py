T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    num_lst = list(map(int, input().split()))
    answer = -1
    for i in range(n):
        for j in range(n-i-1):
            num = num_lst[i] * num_lst[i+1+j]
            if num > answer:
                for z in range(len(str(num))-1):
                    if int(str(num)[z]) > int(str(num)[z+1]):
                        break
                else:
                    answer = num
    print(f'#{tc} {answer}')