# 패션왕 신해빈
for tc in range(int(input())):
    kinds = []
    clothes = []
    for i in range(int(input())):
        cloth, kind = input().split()
        if kind in kinds:
            clothes[kinds.index(kind)].append(cloth)
        else:
            kinds.append(kind)
            clothes.append([cloth])
    answer = 1
    for j in clothes:
        answer *= len(j) + 1

    print(answer - 1)