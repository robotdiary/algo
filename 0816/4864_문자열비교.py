T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 1
    for i in range(len(str2)-len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                cnt += 1
            else:
                break
        if cnt == len(str1):
            result -= 1
            print(f'#{tc} 1')
    if result:
        print(f'#{tc} 0')