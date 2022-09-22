# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 D3
def babygin(arr, p):
    global answer
    # 카드가 세개 미만이면 볼 필요 X
    if len(arr) < 3:
        return
    # sorted하면 바깥의 카드 배열은 바뀌지 않음!
    card = sorted(arr)
    # 같은 카드가 세개면 트리플릿
    for i in range(1, len(card)-1):
        if card[i] == card[i-1] and card[i] == card[i+1]:
            answer = p
    # 같은 카드를 제거해야 순서대로 런인지 확인 가능
    card = list(set(card))
    for i in range(1, len(card)-1):
        if card[i] == card[i-1] + 1 and card[i] == card[i+1] - 1:
            answer = p


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    cards.reverse() # pop(0)하면 오래 걸리니까
    p1 = []
    p2 = []
    answer = 0
    # 카드를 하나씩 가져갈 겁니다.
    while cards:
        p1.append(cards.pop())
        babygin(p1, 1)
        if answer: # 성공하면 break하고 print로
            break
        p2.append(cards.pop())
        babygin(p2, 2)
        if answer:
            break

    print(f'#{tc} {answer}')