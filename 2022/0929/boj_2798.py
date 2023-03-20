# 2789 블랙잭
# def comb():
#     global answer
#
#     if len(sel) == 3:
#         if sum(sel) <= m and answer < sum(sel):
#             answer = sum(sel)
#             return
#     for i in range(3):


n, m = map(int, input().split())  # 카드 수, 최대 수
cards = list(map(int, input().split()))
sel = []
answer = 0
for card1 in range(n):
    for card2 in range(card1 + 1, n):
        for card3 in range(card2 + 1, n):
            if answer < cards[card1] + cards[card2] + cards[card3] <= m:
                answer = cards[card1] + cards[card2] + cards[card3]
print(answer)