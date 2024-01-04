'''
가지 치기로 미리 최대를 측정할 때,
최대는 남은 달걀만큼만 추가되는 게 아니라
남은 계란과 부딪힌 아직 안 깨진(지나간 앞쪽) 계란까지 깨지는 것!
그래서 * 2를 해야함 -> (n - depth) * 2 + acc
'''
def comb(depth, acc):
    global answer
    # 다 돌았거나, 다 깼으면 끝
    if depth == n or acc >= n - 1:
        answer = max(answer, acc)
        return

    # 다 쳐도 안 되면 치지마
    if (n - depth) * 2 + acc <= answer:
        return

    # 손에 든 계란이 깨졌으면 못 쳐
    if eggs[depth][0] <= 0:  # 같다 빼먹었다
        comb(depth + 1, acc)
        return

    # [2] 깨지지 않은 다른 계란이 있으면
    for i in range(n):
        if i != depth and eggs[i][0] > 0:
            # [3] 다른 계란 중에 하나를 친다
            eggs[i][0] -= eggs[depth][1]
            eggs[depth][0] -= eggs[i][1]
            comb(depth + 1, acc + (eggs[i][0] <= 0) + (eggs[depth][0] <= 0))
            eggs[i][0] += eggs[depth][1]
            eggs[depth][0] += eggs[i][1]


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0
comb(0, 0)
print(answer)