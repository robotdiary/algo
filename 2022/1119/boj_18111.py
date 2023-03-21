import math
N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_length = 0
min_length = 567
for i in arr:
    if max(i) > max_length:
        max_length = max(i)
    if min(i) < min_length:
        min_length = min(i)
ceil_length = max_length + math.floor((max_length - min_length) / 2)
floor_length = max_length - math.ceil((max_length - min_length) / 2)
ceil_answer = 0
floor_answer = 0
ceil_inventory = B
floor_inventory = B
# print(ceil_length)
# print(floor_length)
Flag = True
i = 0
while Flag and i < N:
    for j in range(M):
        if arr[i][j] > ceil_length:
            ceil_answer += (arr[i][j] - ceil_length) * 2
            ceil_inventory += 1
        elif arr[i][j] < ceil_length:
            if ceil_inventory < ceil_length - arr[i][j]:
                Flag = False
                break
            else:
                ceil_answer += ceil_length - arr[i][j]
    i += 1
Flag = True
i = 0
while Flag and i < N:
    for j in range(M):
        if arr[i][j] > floor_length:
            floor_answer += (arr[i][j] - floor_length) * 2
            floor_inventory += 1
        elif arr[i][j] < floor_length:
            if floor_inventory < floor_length - arr[i][j]:
                Flag = False
                break
            else:
                floor_answer += floor_length - arr[i][j]
    i += 1
# print(ceil_answer)
# print(floor_answer)
if ceil_answer <= floor_answer:
    print(ceil_answer, ceil_length)
else:
    print(floor_answer, floor_length)