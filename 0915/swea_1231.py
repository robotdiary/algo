#  1231. [S/W 문제해결 기본] 9일차 - 중위순회 (D4)
def inorder(n):
    global answer
    if n:
        inorder(ch1[n])
        answer += tree[n]
        inorder(ch2[n])


for tc in range(1, 11):
    v = int(input())
    ch1 = [0] * (v + 1)
    ch2 = [0] * (v + 1)
    tree = [0] * (v + 1)
    for i in range(v):
        info = list(input().split()) # ['1', 'W', '2', '3']
        if len(info) > 3:
            tree[int(info[0])] = info[1]
            ch1[int(info[0])] = int(info[2])
            ch2[int(info[0])] = int(info[3])
        elif len(info) == 3:
            tree[int(info[0])] = info[1]
            ch1[int(info[0])] = int(info[2])
        else:
            tree[int(info[0])] = info[1]
    answer = ''
    inorder(1)
    print(f'#{tc} {answer}')