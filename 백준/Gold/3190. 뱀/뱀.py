from collections import deque
n = int(input())
# 사과 rc, 시간 int,str 인풋 잘 받았나 확인!
apple = set(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(int(input())))
time, t = [tuple(input().split()) for _ in range(int(input()))], 0
di, dj, d = [0, 1, 0, -1], [1, 0, -1, 0], 0  # 우, 하, 좌, 상
answer, snake = 0, deque([(0, 0)])
while True:
    nr, nc = snake[0][0] + di[d % 4], snake[0][1] + dj[d % 4]
    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in snake:
        snake.appendleft((nr, nc))
        if (nr, nc) not in apple:
            snake.pop()
        else:
            apple.remove((nr, nc))  # 사과 한 번 먹었으면 없어지게
        answer += 1
    else:
        break
    if t < len(time) and int(time[t][0]) == answer:
        if time[t][1] == 'D':
            d += 1
        else:
            d -= 1
        t += 1

print(answer + 1)