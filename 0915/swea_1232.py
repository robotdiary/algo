# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산 (D4)
def inorder(n):
    global answer
    if n:
        inorder(left[n])
        answer.append(tree[n])
        inorder(right[n])
    if len(answer) == 3:
        if answer[1] == '+':
            tree[n] = answer[0] + answer[2]
        elif answer[1] == '-':
            tree[n] = answer[0] - answer[2]
        elif answer[1] == '*':
            tree[n] = answer[0] * answer[2]
        else:
            tree[n] = answer[0] / answer[2]
        answer = []


for tc in range(1, 11):
    v = int(input())
    tree = [0] * (v + 1)     # [0, '-', '-', 10, 88, 65]
    left = [0] * (v + 1)     # [0, 2, 4, 0, 0, 0]
    right = [0] * (v + 1)    # [0, 3, 5, 0, 0, 0]
    parents = [0] * (v + 1)  # [0, 0, 1, 1, 2, 2]
    answer = []
    for i in range(v):
        info = list(input().split())
        if len(info) == 2:
            tree[int(info[0])] = int(info[1])
        else:
            tree[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
            parents[int(info[2])] = int(info[0])
            parents[int(info[3])] = int(info[0])
    inorder(1)
    print(tree[1])


