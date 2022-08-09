T = int(input())
for ts in range(1, T+1):
    N, M = map(int, input().split()) # 숫자의 개수, 몇 구간을 더할지
    v = list(map(int, input().split())) # N=10 M=3 v=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # M 구간의 합을 저장할 빈 리스트 생성
    sum_list = [0] * (N - M + 1)
    # 빈 리스트에 M 구간의 합 저장
    for i in range(N - M + 1): # 0, 1, 2, 3, 4, 5, 6, 7, 8
        for j in range(M): # 0, 1, 2
            sum_list[i] += v[i + j]
    for bs in range(N - M, 0, -1):
        for s in range(0, bs):
            if sum_list[s] > sum_list[s+1]:
                sum_list[s], sum_list[s+1] = sum_list[s+1], sum_list[s]
    print(f'#{ts} {sum_list[-1] - sum_list[0]}')