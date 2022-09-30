# 2115. [모의 SW 역량테스트] 벌꿀채취
for tc in range(1, int(input()) + 1):
    n, m, honey = map(int, input().split())  # 벌통크기, 선택개수, 최대양
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0  # 최대 수익
    ans = 0
    visited = [[], []]
# 일꾼 1 일하기
    for r in range(n):
        for c in range(n-m+1):
            # 연속된 m개의 벌통 선택
            check = arr[r][c:c+m]  # [6, 1]
# 부분집합 부분
            # 선택한 벌통의 부분 집합의 합이 최대 벌꿀보다 작고, 각각의 제곱이 최대일 때 찾기
            for i in range(1 << len(check)):
                selected = []
                visit = set()  # 똑같은 부분 집합들은 또 계산하기 싫다
                for j in range(len(check)):
                    if i & (1 << j):
                        selected.append(check[j])
# 부분집합에서 최대 이익 구하기
                if tuple(selected) not in visit and sum(selected) <= honey:
                    visit.add(tuple(selected))
                    acc = 0
                    for a in selected:
                        acc += a ** 2
                    if acc > answer:
                        answer = acc
# 일꾼 2와 겹치지 않도록 좌표 기억하기
                        visited[0] = r
                        visited[1] = c
# 일꾼 2 일하기
    for r in range(n):
        for c in range(n - m + 1):
# 일꾼 1의 구역이면 continue
            if r == visited[0] and c in range((visited[1] - m + 1), visited[1] + m):
                continue
# 위와 동일
            check = arr[r][c:c + m]
            for i in range(1 << len(check)):
                selected = []
                visit = set()
                for j in range(len(check)):
                    if i & (1 << j):
                        selected.append(check[j])
                if tuple(selected) not in visit and sum(selected) <= honey:
                    visit.add(tuple(selected))
                    acc = 0
                    for a in selected:
                        acc += a ** 2
                    if acc > ans:
                        ans = acc
    print(f'#{tc} {answer + ans}')