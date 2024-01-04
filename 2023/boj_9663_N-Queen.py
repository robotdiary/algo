def recur(depth):  # depth가 곧 가로행
    global answer

    for j in range(n):
        if not c[j] and not left[depth - j] and not right[depth + j]:
            if depth == n - 1:
                answer += 1
                continue
            c[j] = 1
            left[depth - j] = 1
            right[depth + j] = 1
            recur(depth + 1)
            c[j] = 0
            left[depth - j] = 0
            right[depth + j] = 0


n = int(input())
answer = 0
c = [0] * n          # 세로 visited
left = [0] * n * 2   # 왼쪽 대각선 visited
right = [0] * n * 2  # 오른쪽 대각선 visited

recur(0)

print(answer)