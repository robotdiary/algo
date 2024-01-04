'''
오후 4시 15분 - 4시 42분
전에는 turn = [0, 0, 0, 0] 배열을 두고 돌아갈지 적은 채로
for turn으로 rotation을 보냄
지금은 while문 두 개로 바로 돌림
답도 for문 사용 유무로 다르게 뺌
'''
from collections import deque


def rotation(num, d):
    if d == 1:
        chairs[num].appendleft(chairs[num].pop())
    else:
        chairs[num].append(chairs[num].popleft())


chairs = [deque(map(int, input())) for _ in range(4)]
K = int(input())
for tc in range(K):
    N, D = map(int, input().split())  # 1시계 -1반시계
    N -= 1
    current, di = N, D
    # 왼쪽 돌리기
    while 0 <= current - 1:
        if chairs[current][6] != chairs[current - 1][2]:
            current -= 1
            di = -di
        else: break  # 무한돌기

    while current < N:
        rotation(current, di)
        current += 1
        di = -di
    # 오른쪽 돌리기
    while current + 1 < 4:
        if chairs[current][2] != chairs[current + 1][6]:
            current += 1
            di = -di
        else: break

    while current > N:
        rotation(current, di)
        current -= 1
        di = -di
    rotation(N, D)

print(1*chairs[0][0] + 2*chairs[1][0] + 4*chairs[2][0] + 8*chairs[3][0])