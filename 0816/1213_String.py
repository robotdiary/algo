# 그냥 풀기
# for T in range(1, 11):
#     tc = int(input())
#     word = input()
#     sentence = input()
#     answer = sentence.count(word)
#     print(f'#{tc} {answer}')

# BruteForce로 해보자
for T in range(1, 11):
    tc = int(input())
    word = input()
    sentence = input()
    result = 0
    for i in range(len(sentence)-len(word)+1):
        cnt = 0
        for j in range(len(word)):
            if sentence[i+j] == word[j]:
                cnt += 1
            else:
                break
        if cnt == len(word):
            result += 1
    print(f'#{tc} {result}')
