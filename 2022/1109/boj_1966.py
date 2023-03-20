# boj 1966 프린터 큐
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 문서의 개수, 궁금한 서류 번호
    nums = list(map(int, (input().split())))  # [1, 1, 9, 1, 1, 1]
    papers = list(range(N))                   # [0, 1, 2, 3, 4, 5]
    answer = 0
    Flag = True
    while Flag:
        if nums.index(max(nums)):
            nums = nums[1:] + [nums[0]]
            papers = papers[1:] + [papers[0]]
        else:  # 가장 큰 중요도가 가장 앞일 때, 맨 앞 제거
            answer += 1
            if papers[0] == M:
                Flag = False
            nums = nums[1:]
            papers = papers[1:]
    print(answer)