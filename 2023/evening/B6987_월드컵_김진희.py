def world_cup(depth):
    if scores[depth]:
        idx = depth + 1
        while scores[depth]:
            if idx % 6 != depth:
                break
            if scores[idx % 6]:
                scores[idx % 6] -= 1
            idx += 1
            scores[depth] -= 1


answer = [0] * 4
for tc in range(4):
    result = 1
    scores = list(map(int, input().split()))
    same = 0
    win, draw, lose = 0, 0, 0
    # 팀 당 5 경기 확인
    for i in range(0, 17, 3):
        if sum(scores[i:i + 3]) != 5:
            result = 0
            break
        if scores[i + 1]:
            draw += scores[i + 1]
            if not same:
                same = scores[i + 1]
            elif same > 0:
                same -= scores[i + 1]
            else:
                same += scores[i + 1]
            scores[i + 1] = 0  # 나중에 쓰려고 0으로 바꿔
        win += scores[i]
        lose += scores[i + 2]
    if not result:
        answer[tc] = 0
        continue
    # 무승부 확인
    if same:
        answer[tc] = 0
        continue
    # 승패 확인
    if win != lose or draw % 2 or win + (draw // 2) != 15 or lose + (draw // 2) != 15:
        answer[tc] = 0
        continue
    # 여기까지 왔다면 메인 로직을 안 할 수 없지...


    answer[tc] = result
print(*answer)