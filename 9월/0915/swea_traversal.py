#  연습 문제1 - 순회
def preorder(n):
    if n:
        answer.append(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())
e = list(map(int, input().split()))
v = V + 1
ch1 = [0] * v
ch2 = [0] * v
for i in range(V-1):
    p = e[2 * i]
    c = e[2 * i + 1]
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c
answer = []
preorder(1)
print(*answer)