n = int(input())
acup = []  # 대회 점수
bcup = []  # 점수 정렬

final = [0]*n  # 점수 합계
finalcup = []
rank = []
for _ in range(n):
    acup = list(map(int, input().split()))
    bcup = sorted(acup, reverse=True)
    ccup = []  # 순위
    for i in range(n):
        ccup.append(bcup.index(acup[i]) + 1)
        final[i] += acup[i]
    print(*ccup)

finalcup = sorted(final, reverse=True)
for i in range(n):
    rank.append(finalcup.index(final[i]) + 1)
print(*rank)