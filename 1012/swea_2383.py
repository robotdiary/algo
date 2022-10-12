# 2383. [모의 SW 역량테스트] 점심 식사시간
for tc in range(1, int(input()) + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]

    stair1 = []  # 1번 계단 위치
    stair2 = []  # 2번 계단 위치
    person1 = []  # 출구와의 거리
    person2 = []  # 출구와의 거리
    # [1] 계단의 위치 찾기
    for i in range(n):
        for j in range(n):
            if room[i][j] and room[i][j] != 1:
                if not stair1:
                    stair1.append((i, j, room[i][j]))
                else:
                    stair2.append((i, j, room[i][j]))
    # [2] 사람의 위치 찾기
    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                if (abs(i-stair1[0][0]) + abs(j-stair1[0][1])) < (abs(i-stair2[0][0]) + abs(j-stair2[0][1])):
                    person1.append((abs(i-stair1[0][0]) + abs(j-stair1[0][1])))
                elif (abs(i-stair1[0][0]) + abs(j-stair1[0][1])) == (abs(i-stair2[0][0]) + abs(j-stair2[0][1])):
                    if len(person1) < len(person2):
                        person1.append((abs(i - stair1[0][0]) + abs(j - stair1[0][1])))
                    else:
                        person2.append((abs(i - stair2[0][0]) + abs(j - stair2[0][1])))
                else:
                    person2.append((abs(i-stair2[0][0]) + abs(j-stair2[0][1])))
    person1.sort(reverse=True)
    person2.sort(reverse=True)
    answer = 0
    waiting = 0
    if not person2 or person1[0] > person2[0]:
        answer = person1[0] + stair1[0][2]
        for i in range(3, len(person1), 3):
            if person1[i] + stair1[0][2] > person1[i-3]:
                waiting += person1[i] + stair1[0][2] - person1[i-3]
    else:
        answer = person2[0] + stair2[0][2]
        for i in range(3, len(person2), 3):
            if person2[i] + stair2[0][2] > person2[i - 3]:
                waiting += person2[i] + stair2[0][2] - person2[i - 3]
    print(person1)
    print(person2)
    print(answer)
    print(waiting)
    print(f'#{tc} {answer + waiting}')