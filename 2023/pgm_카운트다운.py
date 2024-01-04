import heapq


def solution(target):
    answer = [0, 0]
    q = [(0, 0, target)]  # 던진 수, -불싱글 수, 점수
    while q:
        cnt, ball, num = heapq.heappop(q)
        q, result1, result2, find_answer = push(q, 50, num + 1, 50, num, cnt, ball, 1)
        if find_answer:
            answer[0] += result1
            answer[1] += -result2
            break
        q, result1, result2, find_answer = push(q, 1, min(num + 1, 21), 1, num, cnt, ball, 1)
        if find_answer:
            answer[0] += result1
            answer[1] += -result2
            break
        q, result1, result2, find_answer = push(q, 2, min(41, num+1), 2, num, cnt, ball, 0)
        if find_answer:
            answer[0] += result1
            answer[1] += -result2
            break
        q, result1, result2, find_answer = push(q, 3, min(61, num+1), 3, num, cnt, ball, 0)
        if find_answer:
            answer[0] += result1
            answer[1] += -result2
            break

    return answer


def push(q, start, end, jump, num, cnt, ball, acc):
    for i in range(start, end, jump):
        if num == i:
            return 0, cnt + 1, ball - acc, 1
        elif num < i:continue
        heapq.heappush(q, (cnt + 1, ball - acc, num - i))
    return q, cnt + 1, ball - acc, 0


print(solution(21))
print(solution(58))