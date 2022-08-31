# 4466 최대 성적표 만들기 (d3)
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    stack = []
    for sel in range(k):
        scores.sort()
        score = scores.pop()
        stack.append(score)
    print(f'#{tc} {sum(stack)}')