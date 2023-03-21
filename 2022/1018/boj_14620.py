# 백준 14620 꽃길 (S2)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 987654321
# 꽃1
for i in range(1, n-1):
    for j in range(1, n-1):
        flower1 = [(i, j), (i+1, j), (i, j+1), (i-1, j), (i, j-1)]  # for문 안 돌고 좌표를 찍어줌
        # 꽃2
        for i2 in range(i, n-1):
            for j2 in range(1, n-1):
                flower2 = [(i2, j2), (i2+1, j2), (i2, j2+1), (i2-1, j2), (i2, j2-1)]
                visited = flower1 + flower2
                if len(visited) != len(set(visited)):  # set과 비교해서 길이가 줄면 겹치는 것
                    continue
                # 꽃3
                for i3 in range(i2, n-1):
                    for j3 in range(1, n-1):
                        visited = flower1 + flower2  # visited가 꽃 두 개만 담긴 상태에서 시작
                        flower3 = [(i3, j3), (i3+1, j3), (i3, j3+1), (i3-1, j3), (i3, j3-1)]
                        if len(visited + flower3) != len(set(visited + flower3)):
                            continue
                        visited += flower3      # set해도 15개일때, visited에 추가하고
                        ans = 0                 # 최소값 계산
                        for nr, nc in visited:  # visited의 모든 죄표를 돌면서
                            ans += arr[nr][nc]
                        if ans < answer:
                            answer = ans
print(answer)