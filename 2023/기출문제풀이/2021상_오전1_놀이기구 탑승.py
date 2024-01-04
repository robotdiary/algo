'''
17분컷
'''
N = int(input())
arr = [[0] * N for _ in range(N)]
students = {}
for _ in range(N*N):
    student, n1, n2, n3, n4 = map(int, input().split())
    students[student] = [n1, n2, n3, n4]
    seat = (0, 0, N, N)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                likes = 0
                empty = 0
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 0:
                            empty += 1
                        elif arr[nr][nc] in students[student]:
                            likes += 1
                seat = min(seat, (-likes, -empty, i, j))
    arr[seat[2]][seat[3]] = student

answer = 0
for i in range(N):
    for j in range(N):
        me = arr[i][j]
        cnt = -1
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = i + dr, j + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in students[me]:
                cnt += 1
        if cnt >= 0:
            answer += 10 ** cnt

print(answer)