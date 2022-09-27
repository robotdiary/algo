# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())  # n개의 숫자, k번째 수
    nums = list(input())  # 상자에 적힌 숫자들
    ans = []  # 상자에 적힌 숫자들로 만들 수 있는 모든 수

    # [1] 만들 수 있는 모든 수를 십진수로 넣어두기
    check = 0              # 좌물쇠를 몇 번 돌렸는지
    while check < n // 4:  # 좌물쇠를 n // 4번 돌릴 수 있다.
        for i in range(0, len(nums), n // 4):  # n // 4개씩 숫자 잘라서 10진수로 바꿔 넣기
            ans.append(int(''.join(nums[i:i+(n // 4)]), base=16))
        nums.insert(0, nums.pop())  # 좌물쇠 돌리기 = 맨 뒤 숫자를 맨 앞으로 가져오기
        # print('nums', nums)
        check += 1

    ans.sort(reverse=True)  # 내림 차순으로 나열
    # print('숫자들', ans)
    rank = 1  # k번째 숫자가 나올 때까지 반복
    answer = 0
    for i in range(len(ans)):    # 10진수 수 리스트 전체를 돌면서
        if rank == k:                # k번째 숫자라면
            answer = ans[i]          # 답
            break
        if ans[i+1] < ans[i]:        # 숫자가 작아지면
            rank += 1                # 몇 번째인지 표시해주고

    print(f'#{tc} {answer}')
