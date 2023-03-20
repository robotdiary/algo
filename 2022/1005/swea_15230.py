# swea 15230. 알파벳 공부 (D3)
for tc in range(1, int(input()) + 1):
    text = input()
    answer = 0
    for i in range(len(text)):
        if ord(text[i]) - i == 97:
            answer += 1
        else:
            break
    print(f'#{tc} {answer}')

# T = int(input())
# for tc in range(1, T + 1):
#     text = input()
#     pattern = 'abcdefghijklmnopqrstuvwxyz'
#     p = 0
#     while p < len(text):
#         if text[p] == pattern[p]:
#             p += 1
#         else:
#             break
#     print(f'#{tc} {p}')