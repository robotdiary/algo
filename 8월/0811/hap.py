# listb = []
# for i in range(1<<4):
#     lista = []
#     # 2의 12승 # 0, 1, 10, 11, 110, 111
#     for j in range(4):
#         # 0, 1, 2, 3, 4, 5
#         if i & (1<<j):
#             lista.append(A[j])
#         # 0 & 1 = 0 / 0 & 10 =
#     print(lista)
#     listb.append(lista)
# print(listb)
T = int(input())
A = [z for z in range(1, 13)]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1<<12):
        bubun = []
        for j in range(12):
            if i & (1<<j):
                bubun.append(A[j])
        if len(bubun) == N and sum(bubun) == K:
            count += 1
    print(f'#{tc} {count}')