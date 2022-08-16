# 개수를 카운트 해서 숫자만큼 출력해보자
# T = int(input())
# for tc in range(1, T+1):
#     a, n = map(str, input().split())
#     words = list(map(str, input().split()))
#     numdict = {
#         "ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0,
#         "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0
#     }
#     for word in words:
#         numdict[word] += 1
#     answer = []
#     for key in numdict.keys():
#         for i in range(numdict[key]):
#             answer.append(key)
#     print(f'#{tc}')
#     print(*answer)

# BruteForce로 찾아서 인덱스를 바꿔보자 왜 안 될까???
T = int(input)
for tc in range(1, T+1):
    a, n = map(str, input().split())
    words = list(map(str, input().split()))
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    idx = 0
    for i in range(10):
        for j in range(int(n)):
            if number[i] == words[j]:
                words[idx], words[j] = words[j], words[idx]
                idx += 1
    print(f'# {tc}')
    print(*words)

