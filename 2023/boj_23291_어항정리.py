def build(arr):
    new_arr = []
    for i in zip(*arr):
        new_arr.append(list(i[::-1]))
    return new_arr


def build2(arr):
    left = []
    right = []
    half = len(arr[0]) // 2
    for i in range(len(arr)):
        left.append(arr[i][:half])
        right.append(arr[i][half:])
    turn_left = [left[i][:] for i in range(len(left))]
    for i in range(len(left)):
        for j in range(len(left[0])):
            turn_left[i][j] = left[-1-i][-1-j]
    return turn_left + right


def fish_scaling(n, mx):
    fish = [a[i][:] for i in range(n)]
    for i in range(n):
        for j in range(mx):
            if a[i][j]:
                for dr, dc in (1, 0), (0, 1):  # 중복 조절 안 되게 오른쪽과 아래만
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < mx and a[nr][nc]:
                        d = abs(a[i][j] - a[nr][nc]) // 5
                        if d:
                            if a[i][j] > a[nr][nc]:
                                fish[i][j] -= d
                                fish[nr][nc] += d
                            else:
                                fish[i][j] += d
                                fish[nr][nc] -= d
    return fish


N, K = map(int, input().split())
a = list(map(int, input().split()))
# print('내 어항')
# print(a)
tc = 0
while True:
    mn = min(a)
    # print('큰 어항과 작은 어항의 차이')
    # print(max(a), '-', mn, '=', max(a) - mn)
    if max(a) - mn <= K:
        print(tc)
        break
    # [1] 먼저, 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
    for i in range(len(a)):
        if a[i] == mn:
            a[i] += 1
    # print('작은 어항에 물고기 추가')
    # print(a)

    # [2] 이제 어항을 쌓는다.
    a = [[a[0]], a[1:]]
    while 2 <= len(a) <= len(a[-1]) - len(a[0]):
        a = build([a[i][:len(a[0])] for i in range(len(a))]) + [a[-1][len(a[0]):]]
        # print('어항 쌓기')
        # print(*a, sep='\n')

    # 배열 길이 맞추기
    mx = len(a[-1])
    for i in range(len(a)):
        a[i] += [0] * (mx - len(a[i]))

    # [3] 물고기 수 조절
    n = len(a)
    fish = fish_scaling(n, mx)
    # print('물고기 수 조절')
    # print(*fish, sep='\n')
    # [4] 다시 어항을 바닥에 일렬로
    a = [[]]
    for j in range(mx):
        for i in range(n-1, -1, -1):
            if fish[i][j]:
                a[0].append(fish[i][j])
    # print('어항 한줄로')
    # print(a)
    # 다시 공중 부양
    a = build2(a)
    # print('한 번 공중부양')
    # print(*a, sep='\n')
    a = build2(a)
    # print('두 번 공중부양')
    # print(*a, sep='\n')
    # 여기서 다시 위에서 한 물고기 조절 작업을 수행하고, 바닥에 일렬로 놓는 작업을 수행한다
    mx = len(a[-1])
    n = len(a)
    fish = fish_scaling(n, mx)
    # print('물고기 수 조절')
    # print(*fish, sep='\n')
    a = []
    for j in range(mx):
        for i in range(n - 1, -1, -1):
            if fish[i][j]:
                a.append(fish[i][j])
    # print('내 어항')
    # print(a)
    tc += 1