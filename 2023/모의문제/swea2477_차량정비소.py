'''
sort 안했고
N, M 구분 안 했고
최소값, 최대값 제대로 설정 안 함

창구를 끝나는 시간으로 창구 번호를 갱신하면서 확인하고
그 다음에, 정비를 다시 끝나는 시간으로 갱신하면서 확인하는 방법
'''
from collections import deque

for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())  # 접수수, 정비수, 고객수, 이용번호둘
    A -= 1
    B -= 1
    ai = list(map(int, input().split()))  # 접수창구시간
    bi = list(map(int, input().split()))  # 정비창구시간
    tk = [0] + list(map(int, input().split()))  # 고객 방문 시간

    custs = deque()
    for idx in range(1, len(tk)):
        custs.append((idx, tk[idx]))  # 번호, 도착시간

    desks = [-1] * N
    waiting = []  # 번호, 도착시간, 사용한 창구
    for idx, arrival in custs:  # 손님 한 명씩
        mndesk = N
        mntime = 99999
        for time in range(N):   # 창구 돌면서
            if desks[time] <= arrival:  # 빈 창구 있으면 사용 하고
                desks[time] = arrival + ai[time]
                waiting.append((desks[time], time, idx))
                break
            if desks[time] < mntime:    # 없으면 가장 빠른 창구를 사용
                mndesk = time
                mntime = desks[time]
        else:
            desks[mndesk] += ai[mndesk]
            waiting.append((desks[mndesk], mndesk, idx))

    waiting.sort()
    answer = 0
    desks = [-1] * M
    for arrival, visited, idx in waiting:
        mndesk = M
        mntime = 99999
        for time in range(M):
            if desks[time] <= arrival:  # 빈 창구 있으면 사용 하고
                desks[time] = arrival + bi[time]
                if time == B and visited == A:
                    answer += idx
                break
            if desks[time] < mntime:  # 없으면 가장 빠른 창구를 사용
                mndesk = time
                mntime = desks[time]
        else:
            desks[mndesk] += bi[mndesk]
            if mndesk == B and visited == A:
                answer += idx

    if answer == 0:
        answer = -1
    print(f'#{tc} {answer}')
