# n, k = map(int, input().split())
# if n != k:
#     answer = 0
#     while n != k:
#         if n + (n // 2) > k:
#             n += 1
#         elif n * 2 > k + 1:
#             n -= 1
#         else:
#             n *= 2
#         answer += 1
#     print(answer)
# else:
#     print(0)

# 메모리 초과
from collections import deque
n, k = map(int, input().split())
if n != k:
    stack = deque()
    end = -1
    if n > k:
        stack.append(k)
        end = n
    else:
        stack.append(n)
        end = k
    #bfs
    answer = 0
    visited = {stack[0]}
    while stack:
        for i in range(len(stack)):
            start = stack.popleft()
            if start + 1 == end or start - 1 == end or start * 2 == end:
                answer += 1
                stack = 0
                break
            if start + 1 not in visited and start + 1 < 100000:
                stack.append(start + 1)
                visited.add(start + 1)
            if start - 1 not in visited:
                stack.append(start - 1)
                visited.add(start - 1)
            if start < end and start * 2 < 100000 and start * 2 not in visited:
                stack.append(start * 2)
                visited.add(start * 2)
        else:
            answer += 1
    print(answer)
else:
    print(0)