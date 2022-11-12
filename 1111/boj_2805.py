# 나무자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

top = max(trees)
trees.sort(reverse=True)
answer = 0
cut_acc = [0]
length_acc = [0]
i = 1
Flag = True
while Flag and i < N:
    now = trees[i-1] - trees[i]
    cut_acc.append(now + cut_acc[i-1])
    length_acc.append((now * i) + length_acc[i-1])
    if length_acc[i-1] < M <= length_acc[i]:
        print(length_acc[i-1], length_acc[i])
        if M == length_acc[i]:
            answer = top - cut_acc[i]
            break
        cut = length_acc[i-1]
        for j in range(now):
            next_cut = cut + i
            # print(next_cut)
            if next_cut - M > cut - M >= 0:
                answer = top - cut_acc[i] - j
                Flag = False
            else:
                answer = top - cut_acc[i] - (j + 1)
            cut = next_cut
    i += 1
print(answer)