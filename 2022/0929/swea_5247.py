# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D4
# [2] BFS
from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split()) # 수, 만들 수
    Q = deque([n])
    visited = {n}  # 검색 시간 빠른 set, 시작점 미리 추가
    cnt = 0
    while Q:
        # 몇 번째 연산인지 확인할 수 있는 for문
        for i in range(len(Q)):
            current = Q.popleft()
            if current + 1 not in visited and current + 1 <= 1000000:
                Q.append(current + 1)
                visited.add(current + 1)
            if current - 1 not in visited and current > 0:
                Q.append(current - 1)
                visited.add(current - 1)
            if current * 2 not in visited and current * 2 <= 1000000:
                Q.append(current * 2)
                visited.add(current * 2)
            if current - 10 not in visited and current > 0:
                Q.append(current - 10)
                visited.add(current - 10)
        cnt += 1  # 브레이크 먼저 하면 안 됨 순서 주의
        if m in visited:  # 위에 있어도 되지만 들어가기 전에 하려고
            break

    print(f'#{tc} {cnt}')

# [1] 재귀로 실패 recursion error
# def count(n, cnt):
#     global answer
#     if n == m and cnt < answer:
#         answer = cnt
#         return
#     elif n == m:
#         return
#
#     if cnt + 1 > answer:
#         return
#     if n * 2 not in visited and n * 2 < 1000000:
#         count(n * 2, cnt + 1)
#     if n - 10 not in visited and n - 10 < 1000000:
#         count(n - 10, cnt + 1)
#     if n + 1 not in visited and n + 1 < 1000000:
#         count(n + 1, cnt + 1)
#     if n - 1 not in visited and n - 1 < 1000000:
#         count(n - 1, cnt + 1)
#
#     if n not in visited:
#         visited.add(n)
#
#
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split()) # 수, 만들 수
#     answer = 1000000
#     visited = set()
#     count(n, 0)
#     print(f'#{tc} {answer}')