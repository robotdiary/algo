# 1984. 중간 평균값 구하기 D2
T = int(input())
for tc in range(1, T + 1):
    n = list(map(int, input().split()))
    n.sort()
    nn = n[1:9]
    answer = round(sum(nn)/8)
    print(f'#{tc} {answer}')