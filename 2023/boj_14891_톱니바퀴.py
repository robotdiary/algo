from collections import deque


def rotate(n, di):
    if di == 1:
        first[n].appendleft(first[n].pop())
    elif di == -1:
        first[n].append(first[n].popleft())


first = [deque(input()) for _ in range(4)]  # 문자열
k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    turn = [0, 0, 0, 0]
    turn[num - 1] = direction
    left = num - 1
    right = num - 1
    # 왼쪽 방향 확인
    while 0 <= left - 1:
        if first[left][6] != first[left - 1][2]:
            turn[left - 1] = -turn[left]
            left -= 1
        else:
            break
    # 오른쪽 방향 확인
    while right + 1 < 4:
        if first[right][2] != first[right + 1][6]:
            turn[right + 1] = -turn[right]
            right += 1
        else:
            break
    for d in range(4):
        rotate(d, turn[d])
answer = 0
for i in range(4):
    if first[i][0] == '1':
        answer += 2 ** i

print(answer)
