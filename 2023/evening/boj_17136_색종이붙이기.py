arr = [list(map(int, input().split())) for _ in range(10)]
one = []
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            one.append((i, j))
answer = 25


def cur(depth, cnt, spare, visited):
    global answer
    if sum(cnt) >= answer:
        return

    if not spare:
        answer = min(answer, sum(cnt))

    if depth == len(one):
        return

    cr, cc = one[depth]
    if (cr, cc) not in visited:
        for paper in range(1, 6):
            if cnt[paper] > 4:
                continue
            flag = 0
            visit = set()
            for dr in range(paper):
                for dc in range(paper):
                    nr, nc = cr + dr, cc + dc
                    if arr[nr][nc] != 1 or (nr, nc) in visited:
                        flag = 1
                        break
                    visit.add((nr, nc))
                if flag:
                    break
            else:
                cnt[paper] += 1
                cur(depth + paper, cnt, spare - (paper ** 2), visited | visit)
                cnt[paper] -= 1
    return


cur(0, [0] * 6, len(one), set())
print(answer)
# def cur(depth, visited, used, cnt):
#     global answer
#     # 종료 조건
#     if depth == len(one):
#         if not cnt:
#             answer = min(answer, sum(used))
#         return
#     if not cnt:
#         answer = min(answer, sum(used))
#         return
#     if sum(used) >= answer:
#         return
#
#     i, j = one[depth]
#     if (i, j) not in visited:
#         for paper in range(5, 0, -1):
#             if used[paper] > 4:
#                 continue
#             if i + paper - 1 >= 10 or j + paper - 1 >= 10:
#                 break
#             flag = 0
#             visit = set()
#             for dr in range(paper):
#                 for dc in range(paper):
#                     if not arr[i + dr][j + dc] or (i + dr, j + dc) in visited:
#                         flag = 1
#                         break
#                     visit.add((i + dr, j + dc))
#                 if flag:
#                     break
#             else:
#                 used[paper] += 1
#                 cur(depth + 1, visited | visit, used, cnt - (paper ** 2))
#                 used[paper] -= 1
#     cur(depth + 1, visited, used, cnt)  # 이미 방문한 좌표일 때, 다음 뎁스로 가질 않았음
#
#
# '''
# k번 돌면서 i+k안해줌
# 밑에 하나 더 있었는데 안 해줌
# '''
# arr = [list(map(int, input().split())) for _ in range(10)]
# answer = 25
# one = []
# for i in range(10):
#     for j in range(10):
#         if arr[i][j]:
#             one.append((i, j))
# # print(*arr, sep='\n')
# cur(0, set(), [0] * 6, len(one))
# if answer == 25:
#     print(-1)
# else:
#     print(answer)
#
# # for paper in range(5, 0, -1):
# #     cnt = 5
# #     for i in range(11-paper):
# #         if not cnt:
# #             break
# #         for j in range(11-paper):
# #             if not cnt:
# #                 break
# #             for k in range(paper):
# #                 if arr[i][j:j+paper].count(1) != paper:
# #                     break
# #             else:
# #                 cnt -= 1
# #                 answer += 1
# #                 for k in range(paper):
# #                     arr[i][j:j+paper] = [0] * paper