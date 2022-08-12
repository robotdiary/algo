mail = input()
word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
# test = [i for i in 'CAMBRIDGE']
answer = ''
for i in mail:
    if i in word:
        pass
    else:
        answer += i
print(answer)