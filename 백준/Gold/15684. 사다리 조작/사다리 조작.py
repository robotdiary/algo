'''
사다리를 들고다니지 말고 직접 arr에 comb처럼 넣고 cur갔다가 빼는 방식
사다리가 무조건 오른쪽으로 이어져 있다고 생각함
따라서 맨 오른쪽 열은 사다리가 있을 수 없음 -> m범위 좀 헷갈렸음 IndexError
'''
M, K, N = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().split())
    arr[A-1][B-1] = 1


def check():
    for j in range(M):
        target = j
        for i in range(N):
            if arr[i][target]:
                target += 1
            elif 0 <= target-1 and arr[i][target-1]:
                target -= 1
        if target != j:
            return False
    return True


def cur(depth, start):
    global answer
    if check():
        answer = min(answer, depth)
        return

    if depth == 3:
        return

    if not answer:
        return

    for tc in range(start, N * M):
        i, j = tc // M, tc % M
        if not arr[i][j]:
            if (j==0 or (1 <= j and not arr[i][j-1])) and (j == M-2 or (j < M-2 and not arr[i][j + 1])):
                arr[i][j] = 1
                cur(depth + 1, tc + 1)
                arr[i][j] = 0


answer = 4
cur(0, 0)
print(answer if answer < 4 else -1)