# 1959 두 개의 숫자열
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # 3, 5
    ai = list(map(int, input().split())) # .split() 잘 쓰자
    bj = list(map(int, input().split()))
    answer = 0
    if n < m:
        for i in range(m-n+1):
            cnt = 0
            for j in range(n):
                cnt += ai[j] * bj[i+j]
            if cnt > answer:
                answer = cnt
    else: # m < n
        for i in range(n-m+1):
            cnt = 0
            for j in range(m):
                cnt += bj[j] * ai[i+j]
            if cnt > answer:
                answer = cnt

    print(f'#{tc} {answer}')