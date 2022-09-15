# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree (D2)
# [1] 스택으로 풀어버렸다.
# T = int(input())
# for tc in range(1, T + 1):
#     e, node = map(int, input().split())
#     ch1 = [0] * (e + 2)
#     ch2 = [0] * (e + 2)
#     arr = list(map(int, input().split()))
#     for i in range(0, e*2, 2):
#         if ch1[arr[i]] == 0:
#             ch1[arr[i]] = arr[i + 1]
#         else:
#             ch2[arr[i]] = arr[i + 1]
#     answer = 1
#     ch = [node]
#     while ch:
#         n = ch.pop()
#         if ch1[n]:
#             answer += 1
#             ch.append(ch1[n])
#         if ch2[n]:
#             answer += 1
#             ch.append(ch2[n])
#     print(f'#{tc} {answer}')

# [2] 순회로 풀어보기
def preorder(n):
    global answer
    if n:  #?
        answer += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    e, node = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (e + 2)
    ch2 = [0] * (e + 2)
    for i in range(0, e*2, 2):
        if ch1[arr[i]] == 0:
            ch1[arr[i]] = arr[i + 1]
        else:
            ch2[arr[i]] = arr[i + 1]
    answer = 0
    preorder(node)
    print(f'#{tc} {answer}')