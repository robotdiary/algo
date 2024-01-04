# from collections import deque
#
#
# def cal(command, num):
#     if command == 'D':
#         num *= 2
#         return num % 10000 if num > 9999 else num
#     elif command == 'S':
#         return 9999 if num == 0 else num - 1
#
#     num = '0' * (4 - len(str(num))) + str(num)
#     if command == 'L':
#         return int((num[1:] + num[0]))
#     else:
#         return int(num[-1] + num[:-1])
#
#
# for tc in range(int(input())):
#     n, result = map(int, input().split())
#
#     q = deque([(n, '')])
#     visited = [0] * 10000
#     while q:
#         acc, answer = q.popleft()
#         if acc == result:
#             print(answer)
#             break
#         if visited[acc] == 0:
#             visited[acc] = 1
#             for di in ('D', 'S', 'L', 'R'):
#                 ni = cal(di, acc)
#                 q.append((ni, answer + di))
from collections import deque
import sys
input = sys.stdin.readline


def cal(command, num):
    if command == 'D':
        num *= 2
        return num % 10000 if num > 9999 else num
    elif command == 'S':
        return 9999 if num == 0 else num - 1
    elif command == 'L':
        return 10 * (num % 1000) + num // 1000
    else:
        return 1000 * (num % 10) + num // 10


for tc in range(int(input())):
    n, result = map(int, input().split())

    q = deque([(n, '')])
    visited = [0] * 10000
    while q:
        acc, answer = q.popleft()
        if acc == result:
            print(answer)
            break
        if visited[acc] == 0:
            visited[acc] = 1
            for di in ('D', 'S', 'L', 'R'):
                ni = cal(di, acc)
                q.append((ni, answer + di))