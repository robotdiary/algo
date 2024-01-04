# bfs 아이디어
# from collections import deque
# f, s, g, u, d = map(int, input().split())
# answer = "use the stairs"
#
# q = deque([(s, 0)])
# visited = {s}
# while q:
#     current, push = q.popleft()
#     if current == g:
#         answer = push
#         break
#
#     if u and d:
#         up = current + u
#         down = current - d
#         if up <= f and up not in visited:
#             q.append((up, push + 1))
#             visited.add(up)
#         if down > 0 and down not in visited:
#             q.append((down, push + 1))
#             visited.add(down)
#     elif u:
#         up = current + u
#         if up <= f and up not in visited:
#             q.append((up, push + 1))
#             visited.add(up)
#     elif d:
#         down = current - d
#         if down > 0 and down not in visited:
#             q.append((down, push + 1))
#             visited.add(down)
# print(answer)

# 갈 수 있는 한 쪽으로 최대한 간 후에 하나씩 줄여서 확인하는 아이디어
f, s, g, u, d = map(int, input().split())
answer = "use the stairs"
if s == g:
    answer = 0
else:
    if u and g > s and not (g - s) % u:
        answer = (g - s) // u
    elif d and s > g and not (s - g) % d:
        answer = (s - g) // d
    elif u and d:
        # 위로 가야할 때
        if s < g:
            cnt = abs(g - s) // u
            s += cnt * u
            while 1 <= s - d <= f and s != g:
                s -= d
                cnt += 1
                if abs(g - s) % u == 0:
                    answer = cnt + (abs(g - s) // u)
                    break
            else:
                if cnt:
                    answer = cnt

        # 아래로 갈 때
        else:
            cnt = abs(s - g) // d + 1
            s -= cnt * d
            while 1 <= s + u <= f and s != g:
                s += u
                cnt += 1
                if abs(s - g) % d == 0:
                    answer = cnt + (abs(s - g) // d)
                    break
            else:
                if cnt:
                    answer = cnt
print(answer)

# # 모든 곳을 그냥 가보는 아이디어 -> RecursionError, 메모리 초과
# import sys
# sys.setrecursionlimit(1000000)
# def stairs(currnet, acc):
#     global answer
#     if currnet < 0 or currnet > f:
#         return
#     elif currnet == g:
#         answer = acc
#         return
#
#     if currnet + u not in visited:
#         visited.add(currnet + u)
#         stairs(currnet + u, acc + 1)
#     if currnet - d not in visited:
#         visited.add(currnet - d)
#         stairs(currnet - d, acc + 1)
#
#
# f, s, g, u, d = map(int, input().split())
# answer = "use the stairs"
# visited = {s}
# stairs(s, 0)
# print(answer)
