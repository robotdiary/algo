# start 연습 문제 3
pattern = {
    '001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
    '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9
}
for tc in range(1, int(input()) + 1):
    num = input()
    nums = ''
    for i in num:
        a = int(i, base=16)
        if len(bin(a)[2:]) > 3:
            nums += bin(a)[2:]
        else:
            nums += '0' * (4 - len(bin(a)[2:]))
            nums += bin(a)[2:]
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == '1':
            end = i
            break
    start = end - 5
    answer = []
    while start > 0:
        answer.append(pattern[nums[start:end+1]])
        end = start - 1
        start = end - 5
    answer.reverse()
    print(*answer)