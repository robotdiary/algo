
n = int(input())  # 최대 레벨
characters = list(map(int, input().split()))  # 레벨 별 캐릭터 수
character = sum(characters)  # 총 캐릭터 수
powers = list(map(int, input().split()))  # 레벨 별 파워
d = int(input())  # 훈련 기간
answer = 0
power = [powers[i + 1] - powers[i] for i in range(n-1)]
level = dict()
for k, v in enumerate(power):
    level[v] = k
while d and character == characters[-1]:  # 날짜가 끝났거나 다 키웠을 때 종료
    for p in power:  # 힘이 큰 순으로
        while characters[level[p]] and d:  # 있는 애 모두 성장시키기
            answer += p
            d -= 1
            characters[level[p]] -= 1
            if characters[level[p]] < n - 1:
                characters[level[p] + 1] += 1
        break


print(answer)