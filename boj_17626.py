# 네네무
n = int(input())
first_answer = int(n ** (1/2) // 1)  # 제일 큰 제곱근
testcase = 5
for i in range(first_answer):
    answer = []
    while n > 1:
        n -= (first_answer - i) ** 2
        if len(answer)+1 > testcase:
            answer.append(first_answer)
            print("first_answer", first_answer)
        else:
            break
    if n:
        answer.append(1)
    print(answer)

print(testcase)