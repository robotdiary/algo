# A번 - 치킨댄스를 추는 곰곰이를 본 임스 2
N = int(input())
answer = 0
for _ in range(N):
    target = int(input().lstrip('D-'))
    if target <= 90:
        answer += 1
print(answer)