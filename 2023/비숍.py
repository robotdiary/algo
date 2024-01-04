def bishop(depth, acc):
    global answer
    # if depth % 2:
    #     if odd - (depth // 2) + acc <= answer:
    #         return
    # else:
    #     if even - (depth // 2) + acc + odd <= answer:
    #         return

    if depth <= -n:
        answer = max(answer, acc)
        return

    for b in b_lst[depth]:
        if not visited[b[0] + b[1]]:
            visited[b[0] + b[1]] = 1
            bishop(depth - 2, acc + 1)
            visited[b[0] + b[1]] = 0
    bishop(depth - 2, acc)


n = int(input())
arr = [list(input().split()) for _ in range(n)]  # 문자열 '1', '0'

mx = n * 2 - 1
visited = [0] * mx
odd, even = 0, 0  # 홀, 짝 인덱스의 '1' 개수
b_lst = [[] for _ in range(mx)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            b_lst[i - j].append((i, j))
            if (i - j) % 2:
                odd += 1
            else:
                even += 1
answer = 0
bishop(n - 1, 0)
bishop(n - 2, answer)
print(answer)
