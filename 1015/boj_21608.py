n = int(input())
arr = [[0] * n for _ in range(n)]
information = [list(map(int, input().split())) for _ in range(n ** 2)]
info_dict = {}
# 자리 배정
for info in range(n ** 2):
    student, *like = information[info]
    like = set(like)
    info_dict[student] = like
    if not info:
        arr[1][1] = student
        continue
    status = [0, 0]  # 인접 학생, 빈자리
    sit = [n**2, n**2]  # 앉은 자리
    for i in range(n):
        if 0 not in arr[i]:
            continue
        for j in range(n):
            if arr[i][j]:
                continue
            friend = 0
            side = 0
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + dr < n and 0 <= j + dc < n:
                    if not arr[i + dr][j + dc]:
                        side += 1
                    elif arr[i + dr][j + dc] in like:
                        friend += 1
            if friend > status[0] or friend == status[0] and side > status[1]:
                status = friend, side
                sit = [i, j]
            elif friend == status[0] and side == status[1] and i < sit[0]:
                sit = [i, j]
    arr[sit[0]][sit[1]] = student
# print(arr)
# 만족도 조사
answer = 0
for i in range(n):
    for j in range(n):
        check = -1
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= i + dr < n and 0 <= j + dc < n:
                if arr[i + dr][j + dc] in info_dict[arr[i][j]]:
                    check += 1
        if check >= 0:
            answer += 10 ** check
print(answer)