# 14361. 숫자가 같은 배수 D3
def perm(sel):
    global result
    if len(sel) == len(num) and sel != num and int(sel) % int(num) == 0:
        result = 'possible'
        return
    elif len(sel) == len(num):
        return

    for i in range(len(num)):   # 0,    0, 1, 2  0, 1, 2
        if not check[i]:        # 0     1,0 0    1,1,0
            check[i] = 1        # 1,0,0 1,0,1    1,1,1
            sel += num[i]       # 1     1,2,3    1,2,3
            perm(sel)           #
            check[i] = 0
            sel = sel[:-1]


T = int(input())
for tc in range(1, T + 1):
    num = input() # 문자열
    check = [0]*len(num)
    result = 'impossible'
    answer = []
    perm('')
    print(f'#{tc} {result}')
    # 1035 3105
