def select(x, depth, score):  # 전에 고른거, 몇 번째 문제, 점수
    global answer
    # 가망 없으면 돌려보낸다
    if depth == 6:
        if not score:
            return
    elif depth == 10:
        if score > 4:
            answer += 1
        return

    for i in range(1, 6):
        if i == x:
            continue
        select(i, depth + 1, score + int(exams[depth] == i))
        if depth < 9:
            select(i, depth + 2, score + int(exams[depth] == i) + int(exams[depth + 1] == i))


exams = list(map(int, input().split()))
answer = 0
select(0, 0, 0)
print(answer)