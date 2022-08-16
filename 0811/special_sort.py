T = int(input())
for tc in range(1, T+1):
    n = int(input())
    number = list(map(int, input().split()))
    sortnum = sorted(number)
    answer = []
    ddd = {1:0, 2:0, 3:0}
    for i in range(n//2):
        answer.append(sortnum[-1-i])
        answer.append(sortnum[i])
    if n % 2:
        answer.append(number[n//2])
    # print(f'#{tc} ',end='') 줄 안 바꾸고 출력하기
    # print(*answer[:10]) # 리스트 안의 전체 원소를 가져오기 * !!!!!
    # 그냥 print(answer)하면 출력에서 []가 같이 나온다.
    print(f'#{tc}', *answer[:10])