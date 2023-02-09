# 패션왕 신해빈
import sys
from collections import defaultdict

input = sys.stdin.readline
for tc in range(int(input())):
    n = int(input())

    name_dict = defaultdict()
    clothes = []
    answer = 0

    for _ in range(n):
        name, category = input().split()
        name_dict[name] = category
        clothes.append(name)

    for i in range(1 << n):
        selected = set()
        flag = 1
        for j in range(n):
            if i & (1 << j):
                if name_dict[clothes[j]] in selected:
                    flag -= 1
                    break
                selected.add(name_dict[clothes[j]])
        if flag:
            answer += 1
    print(answer - 1)