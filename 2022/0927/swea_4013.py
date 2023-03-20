# 4013. [모의 SW 역량테스트] 특이한 자석
def magnet(nums, change):
    if change == 1:
        nums.insert(0, nums.pop())
    else:
        nums.append(nums.pop(0))


for tc in range(1, int(input()) + 1):
    k = int(input())  # 회전수
    arr = [list(map(int, input().split())) for _ in range(4)]
    turn = [tuple(map(int, input().split())) for _ in range(k)]
    # 맞닿은 3 7, 3 7, 3 7 번의 극을 확인하고
    # print(arr)
    for clock, d in turn: # 3번 톱니, -1
        check = [0, arr[0][2] ^ arr[1][6], arr[1][2] ^ arr[2][6], arr[2][2] ^ arr[3][6], 0]
        # print(check)
        # 해당 톱니바뀌 돌리기
        n = clock - 1 # 2번 인덱스
        # print(arr[n])
        magnet(arr[n], d)
        # print(arr[n])
        # 반대 방향 변수 설정
        now = d
        oppo = 1
        if now == 1:
            oppo = -1
        # 오른쪽으로 맞닿은 톱니 돌리기
        while check[n + 1]:
            # print(check[n+1])
            # print(now, oppo)
            magnet(arr[n + 1], oppo)
            # print(arr)
            n += 1
            now, oppo = oppo, now
        # 왼쪽으로 맞닿은 톱니 돌리기
        n = clock - 1  # 바뀌었을까봐 초기화
        now = d
        oppo = 1
        if now == 1:
            oppo = -1
        while check[n]:
            magnet(arr[n-1], oppo)
            n -= 1
            now, oppo = oppo, now
        # print(arr)
    answer = 0
    for i in range(4): # 0, 1, 2, 3
        if arr[i][0]:
            answer += 2 ** i
    print(f'#{tc} {answer}')
