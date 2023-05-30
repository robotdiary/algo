from collections import deque


def solution(queue1, queue2):  # 1, 1 / 1, 5
    original = deque(queue2[:])
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    answer = 0
    # 큰 쪽에 있는걸 작은 쪽으로 옮겨
    while True:
        if sum(dq1) == sum(dq2):
            break
        elif sum(dq1) > sum(dq2):
            dq2.append(dq1.popleft())
        else:
            dq1.append(dq2.popleft())
        answer += 1
        if dq1 == original:
            answer = -1
            break
    return answer


print(solution([1, 1], [1, 5]))
