from collections import deque
n, k = map(int, input().split())  # 벨트 한 쪽, 0의 수
a = deque(list(map(int, input().split())))

robots = deque([0] * n)
end = n-1  # 로봇 내리는 지점
cnt = 0  # 0 개수
answer = 0
while cnt < k:
    # 벨트와 로봇 한 칸 이동
    a.appendleft(a.pop())
    robots.pop()
    robots.appendleft(0)
    robots[-1] = 0

    # 로봇 이동
    for i in range(n - 2, 0, -1):
        if robots[i] and not robots[i + 1] and a[i + 1]:
            robots[i] = 0
            if i + 1 != end:
                robots[i + 1] = 1
            a[i + 1] -= 1
            if not a[i + 1]:
                cnt += 1
    # 로봇 추가
    if a[0]:
        robots[0] = 1
        a[0] -= 1
        if not a[0]:
            cnt += 1

    answer += 1
print(answer)