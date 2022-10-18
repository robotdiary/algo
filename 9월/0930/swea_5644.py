# 5644. [모의 SW 역량테스트] 무선 충전
from collections import deque

move = {
    0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)
}

for tc in range(1, int(input()) + 1):
    m, a = map(int, input().split())  # 총 이동 시간, BC의 개수
    amove = list(map(int, input().split()))  # m개, 0 1상 2우 3하 4좌
    bmove = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    bc1 = []  # 좌표

    # 배열 생성
    for _ in range(a):
        x, y, c, p = map(int, input().split())  # 좌표, 충전 범위, 처리량
        q = deque()
        q.append((y-1, x-1))
        visited = [(y-1, x-1)]
        arr[y-1][x-1] = p
        flag = c
        while flag:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = cr + dr
                    nc = cc + dc
                    if 0 <= nr < 10 and 0 <= nc < 10 and (nr, nc) not in visited:
                        if arr[nr][nc] != 0 and [nr, nc] in bc1:
                            arr[nr][nc] = [*arr[nr][nc], p]
                        elif arr[nr][nc] != 0:
                            arr[nr][nc] = [arr[nr][nc], p]
                            bc1.append([nr, nc])
                        elif arr[nr][nc] == 0:
                            arr[nr][nc] = p
                        visited.append((nr, nc))
                        q.append((nr, nc))
            flag -= 1
    bc = []
    for cr, cc in bc1:
        try:
            if len(arr[cr][cc]) > 1:
                bc.append([cr, cc])
        except:
            continue
    # 이동
    # print(arr)
    man = [0, 0]  # arr[man[0]][man[1]]
    woman = [9, 9]  # arr[woman[0]][woman[1]]
    answer = 0
    #arr[man[0]][man[1]] + arr[woman[0]][woman[1]]  # 현재 위치의 충전량
    if arr[man[0]][man[1]] in bc:
        answer += sum(arr[man[0]][man[1]])
    else:
        answer += arr[man[0]][man[1]]
    if arr[woman[0]][woman[1]] in bc:
        answer += sum(arr[woman[0]][woman[1]])
    else:
        answer += arr[woman[0]][woman[1]]

    for i in range(m):
        # 한 칸 이동
        man[0] += move[amove[i]][0]
        man[1] += move[amove[i]][1]
        woman[0] += move[bmove[i]][0]
        woman[1] += move[bmove[i]][1]
        # 충전량 추가
        if arr[man[0]][man[1]] or arr[woman[0]][woman[1]]:
            # [1] 0, 70
            if not arr[man[0]][man[1]] and woman not in bc:
                answer += arr[woman[0]][woman[1]]
            elif not arr[woman[0]][woman[1]] and man not in bc:
                answer += arr[man[0]][man[1]]
            # [2] 0, [70, 40]
            elif not arr[man[0]][man[1]] and woman in bc:
                answer += max(arr[woman[0]][woman[1]])
            elif not arr[woman[0]][woman[1]] and man in bc:
                answer += max(arr[man[0]][man[1]])
            # [3] 70, 40
            elif arr[man[0]][man[1]] and arr[woman[0]][woman[1]] and man not in bc and woman not in bc:
                answer += arr[man[0]][man[1]] + arr[woman[0]][woman[1]]
            # [4] 70, [70, 40, 20] or 20, [70, 40, 20]
            elif arr[man[0]][man[1]] and arr[woman[0]][woman[1]] and man not in bc and woman in bc:
                if arr[man[0]][man[1]] == max(arr[woman[0]][woman[1]]):
                    arr[woman[0]][woman[1]].sort()
                    answer += sum(arr[woman[0]][woman[1]][:2])
                else:
                    answer += arr[man[0]][man[1]] + max(arr[woman[0]][woman[1]])
            elif arr[man[0]][man[1]] and arr[woman[0]][woman[1]] and man in bc and woman not in bc:
                if arr[woman[0]][woman[1]] == max(arr[man[0]][man[1]]):
                    arr[man[0]][man[1]].sort()
                    answer += sum(arr[man[0]][man[1]][:2])
                else:
                    answer += arr[woman[0]][woman[1]] + max(arr[man[0]][man[1]])
            # [5] 40, 40
            elif arr[man[0]][man[1]] == arr[woman[0]][woman[1]] and woman not in bc:
                answer += arr[woman[0]][woman[1]]
            # [6] 리스트 리스트
            elif woman in bc and man in bc:
                # print(man)
                # print(arr[man[0]][man[1]], arr[woman[0]][woman[1]])
                if max(arr[man[0]][man[1]]) == max(arr[woman[0]][woman[1]]):
                    arr[man[0]][man[1]].sort()
                    arr[woman[0]][woman[1]].sort()
                    answer += max(arr[man[0]][man[1]]) + max(arr[man[0]][man[1]][1], arr[woman[0]][woman[1]][1])
                else:
                    answer += max(arr[man[0]][man[1]]) + max(arr[woman[0]][woman[1]])

            # # [0] 각자 다른 곳에 있을 때
            # if arr[man[0]][man[1]] != arr[woman[0]][woman[1]] and man not in bc and woman not in bc:
            #     answer += arr[man[0]][man[1]] + arr[woman[0]][woman[1]]
            # # [1] 두 명이 한 개를 나눠쓰는 경우
            # elif arr[man[0]][man[1]] == arr[woman[0]][woman[1]] and woman not in bc:
            #     answer += arr[woman[0]][woman[1]]
            # # 두 명 다 두 개 위에 있을 때
            # elif arr[man[0]][man[1]] == arr[woman[0]][woman[1]] and man in bc:
            #     answer += sum(arr[man[0]][man[1]])
            # # [3] # 충전 두 개 되는 지역
            # elif not arr[man[0]][man[1]] and woman in bc:
            #     answer += max(arr[woman[0]][woman[1]])
            # elif not arr[woman[0]][woman[1]] and man in bc:
            #     answer += max(arr[man[0]][man[1]])
            # # [2] 한 명은 한 개, 한 명은 두 개
            # elif woman in bc:
            #     # print('woman:', arr[woman[0]][woman[1]])
            #     answer += max(arr[woman[0]][woman[1]]) + arr[man[0]][man[1]]
            # elif man in bc:
            #     answer += max(arr[man[0]][man[1]]) + arr[man[0]][man[1]]
            # # [3] 평범한 경우

    print(f'#{tc} {answer}')
# a = [0, 0, 0, [100, 70], 70, 70, 70, 70, 0, 0]
# print(type(a[3]))
# print(a[3] is not int)
# print(sum(a[3]))