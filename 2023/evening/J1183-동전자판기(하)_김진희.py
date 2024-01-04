def bending_machine(depth, money):  # 6, 13
    global flag
    # 동전 돌기
    for c in range(depth, -1, -1):  # 범위 틀렸다!! 0까지 돌아야하니까 -1까지 !
        # 동전 자체가 금액보다 크면 리턴
        if money - coin[c] < 0:
            return
        # 개수 돌기
        for i in range(coins[c], 0, -1):
            # 동전 개수가 많으면 continue로 개수 - 1
            pay = coin[c] * i
            if money - pay < 0:
                continue
            answer[c] = i
            # 딱 맞으면
            if money - pay == 0:
                flag = 1
                return
            bending_machine(c - 1, money - pay)
            if flag:
                return
            answer[c] = 0


w = int(input())
coin = [500, 100, 50, 10, 5, 1]
coins = list(map(int, input().split()))
flag = 0
answer = [0] * 6
bending_machine(5, w)
print(sum(answer))
print(*answer)