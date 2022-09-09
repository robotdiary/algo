# 2210 숫자판 점프
def comb(r, c, result):
    if len(result) == 6:
        answer.add(tuple(result))
        return
    for z in range(4):
        if 0 <= r+direction[z][0] < 5 and 0 <= c+direction[z][1] < 5:
            result.append(arr[r+direction[z][0]][c+direction[z][1]])
            comb(r+direction[z][0], c+direction[z][1], result)
            result.pop()


direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
arr = [input().split() for _ in range(5)]
answer = set()
for i in range(5):
    for j in range(5):
        comb(i, j, [arr[i][j]])
print(len(answer))

# comb(0, a)
# b= sorted(list(answer))
# print(b)
# set.add()

