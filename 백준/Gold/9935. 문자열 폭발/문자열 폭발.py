words = input()
target = list(input())

answer = []
for i in words:
    answer.append(i)
    if answer[len(answer)-len(target):] == target:
        for j in range(len(target)):
            answer.pop()

if answer:
    print(''.join(answer))
else:
    print('FRULA')