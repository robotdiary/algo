from collections import deque
n = int(input())
apple = set(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(int(input())))
time, t = [tuple(input().split()) for _ in range(int(input()))], 0
di, dj, d = [0, 1, 0, -1], [1, 0, -1, 0], 0  # 우, 하, 좌, 상

# answer가 정답이 되는 게임 시간 == n초
# snake는 뱀의 몸이 있는 위치! -> 맨 뒤의 좌표를 빼고 맨 앞을 좌표를 추가해서 뱀을 이동시킬 것
answer, snake = 0, deque([(0, 0)])
while True:
    nr, nc = snake[0][0] + di[d % 4], snake[0][1] + dj[d % 4]
    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in snake:
        snake.appendleft((nr, nc))
        # 뱀 머리를 추가하고, 사과 못 먹었을 때 꼬리를 뗀다
        if (nr, nc) not in apple:
            snake.pop()
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
# 사과를 set()에 넣어 두고 '''if 좌표 in 사과set():''' 으로 사용했는데,
# 사과를 먹었을 때 좌표를 없애주지 않아서 뱀이 무진장 길어진답니다~