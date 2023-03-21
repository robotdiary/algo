# start 연습문제 2
for tc in range(1, int(input()) + 1):
    num = input()
    nums = ''
    answer = []
    for i in num:
        a = int(i, base=16)
        if len(bin(a)[2:]) > 3:
            nums += bin(a)[2:]
        else:
            nums += '0'*(4-len(bin(a)[2:]))
            nums += bin(a)[2:]
    # print(nums)
    for i in range(0, len(nums), 7):
        answer.append(int(nums[i:i+7], base=2))
    print(*answer)