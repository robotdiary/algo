# 1486. 장훈이의 높은 선반 D4
for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split()) # 점원수, 선반높이
    mans = list(map(int, input().split()))
    answer = sum(mans)
    for i in range(1 << n): # 부분집합의 개수만큼 반복
        sel = []
        for j in range(n):
            if i & (1 << j):
                sel.append(mans[j])
        if sum(sel) >= b:
            answer = min(answer, sum(sel))
    print(f'#{tc} {answer - b}')

