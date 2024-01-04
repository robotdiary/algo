from collections import deque
N, K = map(int, input().split())
arr = deque(map(int, input().split()))
mans = [0] * N
dead = 0
answer = 0
while True:
    if dead >= K:
        break
    # [1] 무빙워크가 한 칸 회전합니다.
    arr.appendleft(arr.pop())
    mans = [0] + mans[:N-1]
    mans[-1] = 0

    # [2] 가장 먼저 무빙워크에 올라간 사람부터 무빙워크 한 칸 이동할 수 있으면 이동
    for i in range(N-1, 0, -1):
        if mans[i] and mans[i+1] == 0 and arr[i+1]:
            mans[i + 1] = mans[i]
            mans[i] = 0
            arr[i+1] -= 1
            if arr[i+1] == 0:
                dead += 1
    # [3] 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
    if arr[0]:
        mans[0] = 1
        arr[0] -= 1
        if arr[0] == 0:
            dead += 1

    answer += 1

print(answer)