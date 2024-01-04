'''
테트리스 블럭 안의 합 최대화하기
백준 - 테트로미노
2시 20분 - 2시 42분 (구현 20분)
'''
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        q = deque([(arr[i][j], i, j, [(i, j)])])
        while q:
            acc, cr, cc, lst = q.popleft()
            if len(lst) == 4:
                answer = max(answer, acc)
                continue
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in lst:
                    q.append((acc + arr[nr][nc], nr, nc, lst+[(nr, nc)]))

di = (1, -1, 0, 0, -1, -1, 1, 1)
dj = (0, 0, 1, -1, -1, 1, -1, 1)
direction = ((1, 2, 3), (4, 1, 5), (4, 3, 6), (1, 3, 0))
for i in range(1, N):
    for j in range(1, M):
        for k in range(4):
            acc = arr[i][j]
            for nd in direction[k]:
                nr, nc = i + di[nd], j + dj[nd]
                if 0 <= nr < N and 0 <= nc < M:
                    acc += arr[nr][nc]
                else:
                    break
            else:
                answer = max(answer, acc)

print(answer)

