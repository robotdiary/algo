test_case = int(input())
for T in range(1, test_case+1):
    cards = list(map(int, input())) # 빈칸이 없으면 그대로 하면 됨
    count = [0] * 12
    triplet = 0
    run = 0
    baby_gin = 0
    for i in range(6):
        count[cards[i]] += 1
    for j in range(12):
        if count[j] > 5:
            triplet += 2
            count[j] -= 6
        elif count[j] > 2:
            triplet += 1
            count[j] -= 3
    for r in range(12):
        if count[r] and count[r+1] and count[r+2]:
            run += 1
            count[r] -= 1
            count[r + 1] -= 1
            count[r + 2] -= 1
    for r in range(12):
        if count[r] and count[r+1] and count[r+2]:
            run += 1
    if triplet + run == 2:
        print(f"#{T} 1")
    else:
        print(f"#{T} 0")