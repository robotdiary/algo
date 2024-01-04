# def snow_white(depth, acc):
#     if depth == 7:
#         if acc == 100:
#             answer = []
#             for i in range(9):
#                 if check[i] == 1:
#                     answer.append(dwarf[i])
#             answer.sort()
#             for height in answer:
#                 print(height)
#             exit(0)
#     for i in range(9):
#         if not check[i]:
#             check[i] = 1
#             snow_white(depth + 1, acc + dwarf[i])
#             check[i] = 0
#
#
# dwarf = []
# for _ in range(9):
#     dwarf.append(int(input()))
# check = [0] * 9
# snow_white(0, 0)
#
# dwarfs = [int(input()) for _ in range(9)]
#
# for i in range(1 << 9):
#     answer = []
#     for j in range(9):
#         if i & (1 << j):
#             answer.append(dwarfs[j])
#     if len(answer) == 7 and sum(answer) == 100:
#         answer.sort()
#         for height in answer:
#             print(height)
#         break

dwarfs = [int(input()) for _ in range(9)]
fake = sum(dwarfs) - 100
answer = 0

dwarfs.sort()
for i in range(8):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == fake:
            answer = (i, j)
for p in range(9):
    if p != answer[0] and p != answer[1]:
        print(dwarfs[p])