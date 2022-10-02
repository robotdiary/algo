# 6자리 숫자에 대해서 완전 검색을 적용해서 Baby-gin을 검사해보시오.
def babygin(depth):
    global answer
    if depth == 6:
        # print(sel)
        if sel[0] == sel[1] == sel[2] and sel[3] == sel[4] == sel[5]:
            answer = True
            return
        elif sel[0] == sel[1] == sel[2] and sel[3] + 1 == sel[4] == sel[5] - 1:
            answer = True
            return
        elif sel[0] + 1 == sel[1] == sel[2] - 1 and sel[3] + 1 == sel[4] == sel[5] - 1:
            answer = True
            return
        else:
            return
    for i in range(6):
        if not check[i]:
            check[i] = 1
            sel[depth] = nums[i]
            babygin(depth + 1)
            check[i] = 0


for tc in range(1, int(input()) + 1):
    nums = list(map(int, input()))
    sel = [0]*6
    check = [0]*6
    answer = False
    babygin(0)
    print(answer)

